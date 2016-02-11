#!/bin/sh

set -o verbose

python3 main.py data/logo.in $@ > data/logo.out
python3 main.py data/right_angle.in $@ > data/right_angle.out
python3 main.py data/learn_and_teach.in $@ > data/learn_and_teach.out
