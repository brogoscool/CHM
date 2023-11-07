import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
y = np.array([0.2, 0.6, 1.1, 1.8, 2.6])

cs = CubicSpline(x, y)

x_new = np.linspace(0, 4, 100)  
y_new = cs(x_new)  

plt.figure()
plt.plot(x, y, "o", label="Табличні дані")
plt.plot(x_new, y_new, label="Кубічний сплайн")
plt.legend()
plt.title("Апроксимація кубічним сплайном")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
