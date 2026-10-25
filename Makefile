PYTHON ?= $(HOME)/.venvs/claude/bin/python
PDFLATEX ?= /opt/local/bin/pdflatex
.PHONY: paper verify
paper:
	PDFLATEX="$(PDFLATEX)" "$(PYTHON)" scripts/build_paper.py
verify:
	"$(PYTHON)" scripts/verify.py
