#!/bin/bash

# change to the root directory of the repository
cd "$(git rev-parse --show-toplevel)"

# install hooks
ln -s ../../hooks/lines.py \
    ../../hooks/changedfiles.py \
    ../../hooks/pre-commit \
    .git/hooks/
