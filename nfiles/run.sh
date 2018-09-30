#!/bin/bash

#SBATCH -o %J.out
#SBATCH -e %J.err
#SBATCH -p main

source /software/pygate/simu8.0.sh
#source /mnt/gluster_NoGPU/wfh/.bashrc
echo 'Run on:' `hostname`
echo 'Start at: ' `date`
echo 'Start MC Simulation at: ' `date`
# cd /hqlf/wfh_2m/sensitivity/6
Gate main.mac
echo 'Finish MC Simulation at: ' `date`
echo 'Finish at: ' `date`

