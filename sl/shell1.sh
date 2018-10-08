#!/bin/bash
# spack load gate
# source <(spack module loads --dependencies gate@7.2)
# source geant4.sh

i=0
n=0
while [ "$i" -lt "$n" ];
do
    echo $i
    cd /home/lvli/Documents/incident/derenzo_trymac &&
    python generate.py "$i" &&
    Gate main.mac
    spack load root@6.10.02
    root .x root2bintxt.C 
    i=`expr $i + 1`
done

