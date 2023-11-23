import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def true_function(x):
    return np.sin(5 * x)


np.random.seed(42)
x_data = np.sort(5 * np.random.rand(100))
y_data = true_function(x_data) + 0.1 * np.random.randn(100)


def model_function(x, a, b, c):
    return a * np.sin(b * x + c)


params, covariance = curve_fit(model_function, x_data, y_data, p0=[1, 5, 0])

x_fit = np.linspace(0, 5, 100)
y_fit = model_function(x_fit, *params)

plt.figure(figsize=(10, 6))

plt.scatter(x_data, y_data, label="Дані з шумом")

plt.plot(x_fit, y_fit, label="Наближення функцією", color="orange")

plt.plot(
    x_fit, true_function(x_fit), label="Справжня функція", linestyle="--", color="gray"
)

plt.title("Метод найменших квадратів")
plt.legend()
plt.show()
