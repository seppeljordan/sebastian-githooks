#!/usr/bin/env python3

import subprocess

def get_changedFiles():
    lines = subprocess.check_output(['git',
                                     'diff',
                                     '--cached',
                                     '--name-only',
                                     'HEAD',
                                     '--'],
                                    universal_newlines=True)
    return lines.split('\n')[:-1]
