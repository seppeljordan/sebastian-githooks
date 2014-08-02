#!/usr/bin/env python3

import subprocess

def _getLines(cmd):
    """Execute string as command and return output as list"""
    lines = subprocess.check_output(cmd.split(), universal_newlines=True)
    return lines.split('\n')[:-1]

def get_changedFiles():
    cmd = "git diff --cached --name-only HEAD --"
    return _getLines(cmd)

def get_allExceptDeletions():
    cmd = "git diff --cached --name-only --diff-filter=ACMRTUX HEAD --"
    return _getLines(cmd)
