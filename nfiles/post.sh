#!/bin/bash

#SBATCH -o %J.out
#SBATCH -e %J.err
#SBATCH -p main

source /software/pygate/simu8.0.sh
echo 'Run on:' `hostname`
echo 'Start at: ' `date`
pygate merge --target result.root --method hadd
#root -q -b result.root Hits2CSV.C
echo 'Finish at: ' `date`

