#!/bin/bash

if [ -d .venv ]; then
    python -m venv .venv
fi

. .venv/bin/activate
pip install -r requirements.txt
