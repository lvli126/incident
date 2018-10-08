#!/bin/bash

i=0
n=1
while [ "$i" -lt "$n" ];
do
    echo $i
    cd /home/lvli/Documents/incident/derenzo &&
    /home/lvli/anaconda3/bin/python generate.py "$i" &&
    Gate main.mac
    spack load root@6.10.02
    root .x .q root2bintxt.C 
    i=`expr $i + 1`
done

