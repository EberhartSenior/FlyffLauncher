#!/bin/bash

# Linux install script for the Flyff Universe launcher

if [ ! -d "../venv/" ]; then
   python3 -m venv ../venv
   ../venv/bin/pip install -r ../requirements.txt
fi

../venv/bin/python ../main.py
