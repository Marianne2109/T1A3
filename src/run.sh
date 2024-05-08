#!/bin/bash

check if python3 is installed
python3 -m venv .venv

check if venv already exists
source .venv/bin/activate

pip3 install -r requirements.txt

clear

python3 main.pyw