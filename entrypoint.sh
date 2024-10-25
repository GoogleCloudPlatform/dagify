#!/bin/bash
if [ "$RUN_MODE" = "ui" ]; then
  cd ui
  uvicorn app:app --host 0.0.0.0 --port 8000
  
elif [ "$RUN_MODE" = "cli" ]; then
  python DAGify.py -r
fi