#!/bin/sh
FILE=$1
cd src/ && python -u main.py --in_file "../input/$FILE.csv" --out_file "../output/$FILE-response.csv"
