import numpy as np 
import pandas as pd 
from pandas import DataFrame

DEFAULT_MATERIAL_FILE = '/home/lvli/Documents/incident/sl/range_material_phantom.dat'
DEFAULT_ACTIVITY_FILE = '/home/lvli/Documents/incident/sl/activity_range_phantom.dat'

intensity1 = np.load('/home/lvli/Documents/incident/sl/intensity.npy')
l = len(intensity1)
materials = ['Air']*l
range_material_phantomD1 = DataFrame([str(l)])
range_material_phantomD2 = DataFrame([intensity1, intensity1, materials]).T
activity_range_phantomD1 = DataFrame([str(l-1)])
activity_range_phantomD2 = DataFrame([intensity1[1:], intensity1[1:], (100*intensity1[1:]).astype('int')]).T
with open(DEFAULT_MATERIAL_FILE, "w") as f1:
    range_material_phantomD1.to_csv(f1, header=False, index=False, sep='\t', mode='a')
    range_material_phantomD2.to_csv(f1, header=False, index=False, sep='\t', mode='a')
with open(DEFAULT_ACTIVITY_FILE,'w') as f2:
    activity_range_phantomD1.to_csv(f2, header=False, index=False, sep='\t', mode='a')
    activity_range_phantomD2.to_csv(f2, header=False, index=False, sep='\t', mode='a')

