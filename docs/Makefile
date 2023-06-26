# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = build
SHAREDDIR_SRC = ../main/docs/shared
SHAREDDIR_DST = $(SOURCEDIR)/shared
REPO_URL      = $(shell git remote get-url origin)

clone_main:
	git clone -b main $(REPO_URL) ../main

copy_shared:
	cp -r $(SHAREDDIR_SRC) $(SHAREDDIR_DST)


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help clone_main copy_shared Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
