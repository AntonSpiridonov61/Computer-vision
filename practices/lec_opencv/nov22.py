import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 4 * np.pi, 300)
A = 1
f = 2
phase = np.pi / 2
s = A * np.sin(t * f + phase)
f2 = 5
s += A * np.sin(t * f2)

f3 = 10
s += A * np.sin(t * f3)

ft = np.fft.rfft(s)
freq = np.fft.rfftfreq(len(s), d=t[1] - t[0])

ift = ft.copy()
ift[freq > 1.0] = 0

srest = np.fft.irfft(ift)

plt.subplot(121)
plt.plot(t, s)
plt.plot(t, srest)
plt.subplot(122)
plt.plot(freq,np.abs(ft))
plt.plot(freq,np.abs(ift))
plt.show()