import numpy as np
import matplotlib.pyplot as plt

xi = np.array([3.5, 3.55, 3.60, 3.65, 3.70, 3.75, 3.80, 3.85, 3.90, 3.95, 4.00])
yi = np.array(
    [
        33.1154,
        34.8133,
        36.5982,
        38.4747,
        40.4473,
        42.5211,
        44.7012,
        46.9931,
        49.4024,
        51.9354,
        54.5982,
    ]
)

x_values = np.array([3.522, 3.905, 3.643, 4.005, 3.675, 3.852])
interpolated_y = []

delta_yi = np.array(
    [1.6979, 1.7849, 1.8765, 1.9726, 2.0738, 2.1801, 2.2919, 2.4093, 2.5330, 2.6628]
)


def newton_interpolation(x, xi, delta_yi):
    n = len(xi)
    result = yi[0]

    for i in range(1, n):
        term = delta_yi[i - 1]
        for j in range(0, i):
            term *= x - xi[j]
        result += term

    return result


for x in x_values:
    interpolated_y.append(newton_interpolation(x, xi, delta_yi))

plt.scatter(xi, yi, label="Дані точки")
plt.plot(x_values, interpolated_y, label="Інтерполяція", color="red")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Інтерполяція за допомогою багаточленів Ньютона")
plt.show()
