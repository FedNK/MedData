import numpy as np
import math
import scipy.fftpack as fftpack

def harmonic(T, dt, f, fi = 0, A = 1):
  w = 2 * math.pi * f
  timevalues = np.linspace(0, T - 1, T)
  result = A * np.cos(timevalues*w + fi)
  return np.array([timevalues, result])

def spec(dt, x):
  signal = fftpack.fft(x)
  frequency = np.linspace(dt, dt*len(x), len(x))
  return np.array([signal, frequency])