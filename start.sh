#!/bin/bash
mitmdump -s Arknights/mitm.py -p 8888 > log/mitm.log 2>&1 &
redis-server --daemonize yes
source venv/bin/activate
python akhelper.py