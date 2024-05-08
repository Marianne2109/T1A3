#!/bin/bash

#create a virtual environment
python3 -m venv .venv

#activate the virtual environment
source .venv/bin/activate

#install the required packages
pip3 install -r requirements.txt

clear

#run the main.py file
python3 main.py