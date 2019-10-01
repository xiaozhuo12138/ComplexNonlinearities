#%%
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from Hysteresis import Hysteresis_Process

#%%
def plotSineResponse (func, freq=100, seconds=1, fs=44100):
    n = np.arange (fs * seconds)
    x = np.sin (2 * np.pi * n * freq / fs)
    y = func (x)
    plt.plot (x[1000:], y[1000:])

def plotRisingSineResponse (func, freq=100, seconds=0.1, fs=44100):
    N = fs * seconds
    n = np.arange (N)
    x = np.sin (2 * np.pi * n * freq / fs) * (n/N)
    y = func (x)
    plt.plot (x, y)

#%%
drive = [1] # [0, 0.25, 0.5, 0.75, 1]
width = [0]
saturation = [0] # [0, 0.25, 0.5, 0.75, 1]
fs = 44100

plt.figure()
for sat in saturation:
    for d in drive:
        for w in width:
            gain = 1 # 1e4
            M_s = gain * (0.5 + 1.5*(1-sat)) # saturation
            a = M_s / (0.01 + 6*d) #adjustable parameter
            alpha = 1.6e-3

            k = 30 * (1-0.5)**6 + 0.01 # Coercivity
            c = (1-w)**0.5 - 0.01 # Changes slope
            makeup = (1 + 0.6*w) / (0.5 + 1.5*(1-sat))
            plotRisingSineResponse (lambda x : makeup * Hysteresis_Process (gain*x, M_s, a, alpha, k, c, 1/fs), fs=fs)


#%%
n = np.linspace (0, 1)
y = n**0.5
plt.plot (n, y)


#%%