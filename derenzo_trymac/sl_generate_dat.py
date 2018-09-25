import numpy as np 
import pandas as pd 
from pandas import DataFrame

DEFAULT_MATERIAL_FILE =
intensity1 = np.load('/home/lvli/Documents/incident/voxelized_phantom_trymac/intensity1.npy')
l = len(intensity1)
materials = ['Air']*l
range_material_phantomD1 = DataFrame([str(l)])
range_material_phantomD2 = DataFrame([intensity1, intensity1, materials]).T
activity_range_phantomD = DataFrame([intensity1, intensity1, intensity1]).T
with open(DEFAULT_MATERIAL_FILE, "w") as f:
    range_material_phantomD1.to_csv(f, header=False, index=False, sep='\t', mode='a')
    range_material_phantomD2.to_csv(f, header=False, index=False, sep='\t', mode='a')
with open(DEFAULT_ACTIVITY_FILE,'w') as f:
    activity_range_phantomD.to_csv('/home/lvli/Documents/incident/derenzo_trymac/activity_range_phantomD.dat', header=False, index=False, sep='\t', mode='a')

# print(activity_range_phantomD)