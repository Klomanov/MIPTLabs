import matplotlib.pyplot as plt
import numpy as np
from ApproximationError import app_err

Y_arr = np.array([0.318, 0.492, 0.658, 0.824, 0.987, 1.153, 1.318, 1.482])/1000
X_arr = np.array([20, 30, 40, 50, 60, 70, 80, 90])/100/1000

for i in range(len(X_arr)):
    plt.errorbar(X_arr[i], Y_arr[i], xerr=1/100/1000, yerr=0.002/1000, color="red")

[k, b], cov = np.polyfit(X_arr, Y_arr, 1, cov=True)
arg = np.array([0, 1.5/100])
func = lambda x: k*x + b
plt.plot(X_arr, func(X_arr))

print("R = {k} +- 0.01".format(k=round(k, 2)))
plt.show()