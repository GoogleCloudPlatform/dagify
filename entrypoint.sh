#!/bin/bash
if [ -n "$RUN_MODE" ]; then
  if [ "$(echo "$RUN_MODE" | tr '[:upper:]' '[:lower:]')" = "ui" ]; then
    cd ui
    uvicorn app:app --host 0.0.0.0 --port 8000
  else
    echo "Error: Invalid value for RUN_MODE. Use 'ui' or omit the flag to run the CLI."
    exit 1
  fi
else
  python DAGify.py "$@" # Pass additional arguments (-r) DAGify.py
fi