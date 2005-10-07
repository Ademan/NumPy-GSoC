"""
Discrete Fourier Transforms - FFT.py 

The underlying code for these functions is an f2c translated and modified
version of the FFTPACK routines.

fft(a, n=None, axis=-1) 
inverse_fft(a, n=None, axis=-1) 
real_fft(a, n=None, axis=-1) 
inverse_real_fft(a, n=None, axis=-1)
hermite_fft(a, n=None, axis=-1)
inverse_hermite_fft(a, n=None, axis=-1)
fftnd(a, s=None, axes=None)
inverse_fftnd(a, s=None, axes=None)
real_fftnd(a, s=None, axes=None)
inverse_real_fftnd(a, s=None, axes=None)
fft2d(a, s=None, axes=(-2,-1)) 
inverse_fft2d(a, s=None, axes=(-2, -1))
real_fft2d(a, s=None, axes=(-2,-1)) 
inverse_real_fft2d(a, s=None, axes=(-2, -1))
"""
from fft_lite import *

ifft = inverse_fft
rfft = real_fft
irfft = inverse_real_fft
hfft = hermite_fft
ihfft = inverse_hermite_fft

fftn = fftnd
ifftn = inverse_fftnd
rfftn = real_fftnd
irfftn = inverse_real_fftnd

fft2 = fft2d
ifft2 = inverse_fft2d
rfft2 = real_fft2d
irfft2 = inverse_real_fft2d

from helper import *
