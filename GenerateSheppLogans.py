import numpy as np
from scipy.misc import imrotate, bytescale
from phantom import phantom
from _imrotate import _imrotate
import cv2
import matplotlib.pyplot as plt

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
    X2list = img.flatten().tolist()    
    intensity = list(set(X2list))
    intensity.sort(key = X2list.index)
    print(intensity)
    return X, intensity
#the first column of E is indensity
phantom1, intensity = GenerateSheppLogans(1, 256, 0.1)
print(intensity)

phantom1.astype('float32').tofile('/home/lvli/Documents/incident/voxelized_phantom_trymac/phantom1.bin')
np.save('/home/lvli/Documents/incident/voxelized_phantom_trymac/intensity1.npy',intensity)

