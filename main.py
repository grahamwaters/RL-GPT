#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script generates Sphinx documentation for the RL-GPT project.

Usage:
    python generate_docs.py
"""

import os
import subprocess

# Paths to source and documentation directories
SRC_DIR = os.path.abspath('.')
DOCS_DIR = os.path.abspath('docs')

# Generate API documentation using Sphinx-apidoc
subprocess.call(['sphinx-apidoc', '-o', DOCS_DIR, SRC_DIR, '--force'])

# Generate HTML documentation using Sphinx-build
subprocess.call(['sphinx-build', '-b', 'html', '-d', os.path.join(DOCS_DIR, '_build', 'doctrees'), DOCS_DIR, os.path.join(DOCS_DIR, '_build', 'html')])
