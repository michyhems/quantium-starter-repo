#!/bin/bash

source "./venv/Scripts/activate"

pytest task5.py
pytest_exit_status=$?
if [ $pytest_exit_status -eq 0 ]; then
  exit 0
else
  exit 1
fi
