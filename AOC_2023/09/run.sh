#!/bin/bash
source ../.venv/bin/activate
watchmedo shell-command \
    --drop --wait \
    --patterns="*.py" \
    --command="clear && python solve.py" \
    .
