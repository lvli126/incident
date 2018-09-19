import numpy as np
import string
import math
# from PIL import Image
# from pylab import *


def phantom(*kargs):
    ellipse, n = parse_inputs(*kargs)
    p = np.zeros((n, n))
    xax = np.array([(i-(n-1)/2) / ((n-1)/2) for i in range(n)])
    xg = np.tile(xax, (n,1))
    for k in range(len(ellipse)):
        asq = ellipse[k,1]**2
        bsq = ellipse[k,2]**2
        phi = ellipse[k,5]*math.pi / 180
        x0 = ellipse[k,3]
        y0 = ellipse[k,4]
        A = ellipse[k,0]
        x = xg - x0
        y = xg.T[::-1] - y0
        # y = xg.T - y0
        cosp = math.cos(phi)
        sinp = math.sin(phi)
        con = (x*cosp + y*sinp)**2 / asq + (y*cosp + x*sinp)**2 / bsq
        index_x, index_y = np.where(con <= 1)
        # print(index)
        for idx_x, idx_y in zip(index_x, index_y):
            p[idx_x, idx_y] = p[idx_x, idx_y] + A
    # print(p[:,100])
    return p

def parse_inputs(*kargs):
    n = 256
    e = []
    defaults = ['shepp-logan', 'modified shepp-logan']
    for arg in kargs:
        if isinstance(arg, str):
            arg = arg.lower()
            idx = defaults.index(arg)
            if not idx:
                raise IOError
            elif idx == 0:
                e = shepp_logan
            elif idx == 1:
                e = modified_shepp_logan
        elif isinstance (arg, int):
            n = arg
        elif (arg.ndim == 2) and (arg.shape[1] == 6):
            e = arg 
        else:
            raise IOError

    if not len(e):
        e = modified_shepp_logan
    return e, n


#                          A    a       b      x0     y0   phi
shepp_logan = np.array([[  1,  .69,     .92,    0,     0,  0],   
                        [-.98, .6624, .8740,    0,-.0184,  0],
                        [-.02, .1100, .3100,  .22,     0,-18],
                        [-.02, .1600, .4100, -.22,     0, 18],
                        [ .01, .2100, .2500,    0,   .35,  0],
                        [ .01, .0460, .0460,    0,    .1,  0],
                        [ .01, .0460, .0460,    0,   -.1,  0],
                        [ .01, .0460, .0230, -.08, -.605,  0],
                        [ .01, .0230, .0230,    0, -.606,  0],
                        [ .01, .0230, .0460,  .06, -.605,  0]])


modified_shepp_logan =np.array([[ 1,   .69,   .92,     0,     0,     0],   
                                [-.8,  .6624,  .8740,   0,  -.0184,   0],
                                [-.2,  .1100,  .3100,  .22,    0,   -18],
                                [-.2,  .1600,  .4100, -.22,    0,    18],
                                [ .1,  .2100,  .2500,   0,   .35,     0],
                                [ .1,  .0460,  .0460,   0,    .1,     0],
                                [ .1,  .0460,  .0460,   0,   -.1,     0],
                                [ .1,  .0460,  .0230, -.08,  -.605,   0], 
                                [ .1,  .0230,  .0230,   0,   -.606,   0],
                                [ .1,  .0230,  .0460,  .06,  -.605,   0]])
