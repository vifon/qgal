#!/bin/bash

# Dereference all the symlinks and call the real application. It's
# important because Flask needs to know where to look for its
# resources.

exec "$(dirname "$(readlink -f "$0")")"/ImgServe.py "$@"
