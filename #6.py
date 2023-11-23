import numpy as np
import matplotlib.pyplot as plt

x = np.array([-2, -1, 2, 3])
f_x = np.array([-22, -10, -10, -2])

x_interp = np.array([-1.5, -0.5, 1.5, 2.5])
f_interp = np.zeros(len(x_interp))

def lagrange_interpolation(x, f_x, x_interp):
    n = len(x)
    m = len(x_interp)
    result = np.zeros(m)

    for i in range(m):
        for j in range(n):
            L = 1
            for k in range(n):
                if k != j:
                    L *= (x_interp[i] - x[k]) / (x[j] - x[k])
            result[i] += f_x[j] * L

    return result

f_interp = lagrange_interpolation(x, f_x, x_interp)

for i in range(len(x_interp)):
    print(f'({x_interp[i]}) = {f_interp[i]:.3f}')

plt.figure(figsize=(8, 6))
plt.scatter(x, f_x, label='Дані точки', color='red')
plt.plot(x_interp, f_interp, label='Інтерполяційна функція', linestyle='dashed', color='blue')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.title('Інтерполяційна функція Лагранжа')
plt.show()
