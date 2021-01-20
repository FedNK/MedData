import scipy.fftpack as fftpack
import numpy as np

def spec(dt, x):
  n = len(x)
  k = np.arange(n)
  T = n/dt
  frq = k/T
  frq = frq[range(n/2)]
  Y = fftpack.fft(x)/n
  Y = Y[range(n/2)]
  return x