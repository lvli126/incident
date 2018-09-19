import numpy
import tempfile

from numpy import (amin, amax, ravel, asarray, arange, ones, newaxis,
                   transpose, iscomplexobj, uint8, issubdtype, array)
from scipy.misc import toimage, fromimage

def _imrotate(arr, mode, angle, interp='bilinear'):
    """
    Rotate an image counter-clockwise by angle degrees.
    This function is only available if Python Imaging Library (PIL) is installed.
    .. warning::
        This function uses `bytescale` under the hood to rescale images to use
        the full (0, 255) range if ``mode`` is one of ``None, 'L', 'P', 'l'``.
        It will also cast data for 2-D images to ``uint32`` for ``mode=None``
        (which is the default).
    Parameters
    ----------
    arr : ndarray
        Input array of image to be rotated.
    angle : float
        The angle of rotation.
    interp : str, optional
        Interpolation
        - 'nearest' :  for nearest neighbor
        - 'bilinear' : for bilinear
        - 'lanczos' : for lanczos
        - 'cubic' : for bicubic
        - 'bicubic' : for bicubic
    Returns
    -------
    imrotate : ndarray
        The rotated array of image.
    """
    arr = asarray(arr)
    func = {'nearest': 0, 'lanczos': 1, 'bilinear': 2, 'bicubic': 3, 'cubic': 3}
    im = toimage(arr, mode = mode)
    im = im.rotate(angle, resample=func[interp])
    return fromimage(im)