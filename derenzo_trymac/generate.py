import tables
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd
import numpy as np

DEFAULT_MATERIAL_FILE = '/home/lvli/Documents/incident/derenzo_trymac/range_material_phantomD.dat'
DEFAULT_ACTIVITY_FILE = '/home/lvli/Documents/incident/derenzo_trymac/activity_range_phantomD.dat'

f = tables.open_file('/home/lvli/derenzo.h5')
derenzo, value = f.root.derenzo.derenzo[1907]
a = [0, value[0], value[1]]
b = [0, value[0], value[1]]
c = ['Air', 'Water', 'LSO']
range_material_phantomD1 = DataFrame([str(3)])
range_material_phantomD2 = DataFrame([a,b,c]).T
activity_range_phantomD = DataFrame([[2,value[0],value[1]], [np.nan, value[0], value[1]], [np.nan, int(10*value[0]), int(10*value[1])]]).T
derenzo.tofile("/home/lvli/Documents/incident/derenzo_trymac/phantomD.bin")
with open(DEFAULT_MATERIAL_FILE, "w") as f:
    range_material_phantomD1.to_csv(f, header=False, index=False, sep='\t', mode='a')
    range_material_phantomD2.to_csv(f, header=False, index=False, sep='\t', mode='a')
with open(DEFAULT_ACTIVITY_FILE,'w') as f:
    activity_range_phantomD.to_csv('/home/lvli/Documents/incident/derenzo_trymac/activity_range_phantomD.dat', header=False, index=False, sep='\t', mode='a')


