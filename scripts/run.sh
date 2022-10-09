#!/bin/sh
FILE=$1
ENGINE=$2
cd src/ && python -u main.py --engine "$ENGINE" --in_file "../input/$FILE.csv" --out_file "../output/$FILE-$ENGINE.csv"
