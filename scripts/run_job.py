"""Tracked bounded subprocess runner; invoke with the selected venv interpreter."""
import argparse, json, os, pathlib, resource, signal, subprocess, sys, time
assert sys.prefix != sys.base_prefix
p=argparse.ArgumentParser(); p.add_argument('name'); p.add_argument('--cpu',type=int,required=True); p.add_argument('--wall',type=int,required=True); p.add_argument('command',nargs=argparse.REMAINDER)
a=p.parse_args(); cmd=a.command; cmd=cmd[1:] if cmd and cmd[0]=='--' else cmd
root=pathlib.Path(__file__).resolve().parents[1]; job=root/'build'/'jobs'/a.name; job.mkdir(parents=True,exist_ok=False)
env=dict(os.environ)
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']: env[key]='1'
def limits():
    os.setsid(); resource.setrlimit(resource.RLIMIT_CPU,(a.cpu,a.cpu+1))
start=time.monotonic()
with (job/'output.log').open('w') as out:
    proc=subprocess.Popen(cmd,cwd=root,env=env,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
    record={'pid':proc.pid,'runner_pid':os.getpid(),'command':cmd,'cpu_cap':a.cpu,'wall_cap':a.wall,'status':'RUNNING'}
    (job/'job.json').write_text(json.dumps(record,indent=2)); print(json.dumps(record),flush=True)
    killed=False
    while True:
        pid,status,usage=os.wait4(proc.pid,os.WNOHANG)
        if pid: break
        if time.monotonic()-start>a.wall:
            os.killpg(proc.pid,signal.SIGKILL); killed=True
            pid,status,usage=os.wait4(proc.pid,0); break
        time.sleep(0.25)
    try: os.kill(proc.pid,0); alive=True
    except ProcessLookupError: alive=False
    record.update(status='DONE',wait_status=status,exit_code=os.waitstatus_to_exitcode(status),cpu_seconds=usage.ru_utime+usage.ru_stime,wall_seconds=time.monotonic()-start,max_rss=usage.ru_maxrss,killed=killed,pid_alive_after_wait=alive)
    (job/'job.json').write_text(json.dumps(record,indent=2)); print(json.dumps(record),flush=True)
    sys.exit(record['exit_code'] if record['exit_code']>=0 else 1)
