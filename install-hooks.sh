#!/bin/bash

ln -s ../../hooks/lines.py \
    ../../hooks/changedfiles.py \
    ../../hooks/pre-commit \
    .git/hooks/
