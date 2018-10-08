import tables
import numpy as np
from pandas import DataFrame
import sys

DEFAULT_MATERIAL_FILE = '/home/lvli/Documents/incident/sl/range_material_phantom.dat'
DEFAULT_ACTIVITY_FILE = '/home/lvli/Documents/incident/sl/activity_range_phantom.dat'
DEFAULT_PHANTOM_FLIE = '/home/lvli/Documents/incident/sl/phantom.bin'
def trim(input_array, trim = -1):
    return input_array[~np.in1d(input_array, trim).reshape(input_array.shape)]

def rescale(input_array, scale=255):
    return input_array/scale

f = tables.open_file('/home/lvli/S_1.h5')
# print(int(sys.argv[0]), type(int(sys.argv[0])))
intensity, shepplogan= f.root.sheppLogans[int(sys.argv[1])]
intensity = rescale(trim(intensity,-1))#normalization
shepplogan = rescale(shepplogan)
shepplogan.tofile(DEFAULT_PHANTOM_FLIE)
l = len(intensity)
materials = ['Air']*l
intensity_sort1 = intensity[np.argsort(intensity)].astype('float32')
intensity_sort2 = np.append(intensity_sort1[1:], np.array([1.5])).astype('float32')
act_intensity = [[str(i) for i in intensity_sort1], [str(i) for i in intensity_sort2], [str(int(100*i)) for i in intensity_sort1]]
range_material_phantomD1 = DataFrame([str(l)])
range_material_phantomD2 = DataFrame([intensity_sort1, intensity_sort2, materials]).T
activity_range_phantomD1 = DataFrame([str(l)])
activity_range_phantomD2 = DataFrame(act_intensity).T

with open(DEFAULT_MATERIAL_FILE, "w") as f1:
    range_material_phantomD1.to_csv(f1, header=False, index=False, sep='\t', mode='a')
    range_material_phantomD2.to_csv(f1, header=False, index=False, sep='\t', mode='a')
with open(DEFAULT_ACTIVITY_FILE,'w') as f2:
    activity_range_phantomD1.to_csv(f2, header=False, index=False, sep='\t', mode='a')
    activity_range_phantomD2.to_csv(f2, header=False, index=False, sep='\t', mode='a')