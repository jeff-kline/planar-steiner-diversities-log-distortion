PYTHON ?= python3
PDFLATEX ?= pdflatex
.PHONY: paper verify
paper:
	PDFLATEX="$(PDFLATEX)" "$(PYTHON)" scripts/build_paper.py
verify:
	"$(PYTHON)" scripts/verify.py
