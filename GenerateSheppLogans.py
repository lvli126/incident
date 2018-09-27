import numpy as np
from scipy.misc import imrotate, bytescale
from phantom import phantom
from _imrotate import _imrotate
import cv2
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# import numpy as np 
import pandas as pd 
from pandas import DataFrame


def GenerateSheppLogans(Nimg, Nsize, sigma):
# GENERATESHEPPLOGANS Generaing multiple shapplogan phantoms.
# Suggest sigma = 0.1, plotwindow = [0.9 1.1]
    Em = np.zeros((10, 6))
    Em[:,0] = [1, -0.98, -0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
    Em[:,1] = [0.69, 0.6624, 0.11, 0.16, 0.21, 0.046, 0.046, 0.046, 0.023, 0.023]
    Em[:,2] = [0.92, 0.874, 0.31, 0.41, 0.25, 0.046, 0.046, 0.023, 0.023, 0.046]
    Em[:,3] = [0, 0, .22, -.22, 0, 0, 0, -.08, 0, .06]
    Em[:,4] = [0, -.0184, 0, 0, .35, .1, -.1, -.605, -.605, -.605]
    Em[:,5] = [0, 0, -18, 18, 0, 0, 0, 0, 0, 0]
    sigmac = [0.1, 1, 1, 1, 1, 10]
    X = np.zeros((Nsize, Nsize, Nimg))
    for i in range(Nimg):
        E = np.random.randn(10,6)
        E = E*Em*sigma
        for j in range(6):
            E[:,j] = E[:, j] * sigmac[j]
        E = E + Em
        img = phantom(E, Nsize)
        img = imrotate(img, sigma*10*np.random.randn(),'nearest')
        X[:,:,i] = img
    
    min_max_scaler = MinMaxScaler((0,1))
    phantomX = np.reshape((min_max_scaler.fit_transform(X[:,:,i].reshape((1,Nsize*Nsize)).T)),(Nsize, Nsize))
    X2list = phantomX.flatten().tolist()
    intensity = list(set(X2list))
    intensity.sort(key = X2list.index)
    # print(intensity)
    return phantomX, intensity
phantom1, intensity = GenerateSheppLogans(1, 256, 0.1)
# print(intensity)
np.save('/home/lvli/Documents/incident/sl/phantom.npy', phantom1.astype('float32'))
phantom1.astype('float32').tofile('/home/lvli/Documents/incident/sl/phantom.bin')
np.save('/home/lvli/Documents/incident/sl/intensity.npy',intensity)



DEFAULT_MATERIAL_FILE = '/home/lvli/Documents/incident/sl/range_material_phantom.dat'
DEFAULT_ACTIVITY_FILE = '/home/lvli/Documents/incident/sl/activity_range_phantom.dat'

intensity1 = np.load('/home/lvli/Documents/incident/sl/intensity.npy')
l = len(intensity1)
intensity1 = intensity1.astype('float32')
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

