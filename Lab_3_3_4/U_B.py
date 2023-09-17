import numpy as np
from matplotlib import pyplot as plt

I = np.array([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3])
U_hall = np.array([0.101, 0.125, 0.139, 0.151, 0.161, 0.174])/1000
B = np.array([533, 594, 674, 731, 790, 856])/1000

for i in range(len(I)-1):
    plt.errorbar(B[i], U_hall[i], xerr=2/1000, yerr=0.002/1000, color='red')

[k, b], cov = np.polyfit(B, U_hall, 1, cov=True)
arg = np.linspace(B[0]*0.9, B[-1]*1.1, 100)
func = lambda x: k*x + b
plt.plot(arg, func(arg))
plt.xlim(B[0]*0.95, B[-1]*1.05)
plt.xlabel("B", loc="right")
plt.ylabel("U", loc="top")

print(k)
plt.show()
