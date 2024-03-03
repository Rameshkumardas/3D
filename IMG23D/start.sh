#!/bin/bash
 
echo "Container Started"
export PYTHONBUFFERED=1
echo "Starting Worker"
python3 -u TXT23Dserver.py
python3 -u handler.py