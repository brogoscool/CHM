import numpy as np
import matplotlib.pyplot as plt

def eq1(x, y):
    return np.sin(x + 0.5) - y - 1

def eq2(x, y):
    return np.cos(y - 2) + x

tolerance = 0.001

x0, y0 = 0, 0

def phi1(x, y):
    return y + np.sin(x + 0.5) - 1

def phi2(x, y):
    return 2 - np.cos(y) - x

def phi1_dx(x, y):
    return 1.0

def phi1_dy(x, y):
    return np.cos(x + 0.5)

def phi2_dx(x, y):
    return -1.0

def phi2_dy(x, y):
    return np.sin(y)

def check_convergence(x, y):
    return max(abs(phi1_dx(x, y) + phi2_dy(x, y)), abs(phi2_dx(x, y) - phi1_dy(x, y)))

iterations = 0
while True:
    x1 = phi1(x0, y0)
    y1 = phi2(x0, y0)
    iterations += 1

    if check_convergence(x1, y1) < 1:
        x0, y0 = x1, y1
        if eq1(x0, y0) < tolerance and eq2(x0, y0) < tolerance:
            break
    else:
        print("The method doesn't match.")
        break

print(f"Found roots: x = {x0}, y = {y0}")
print(f"Number of iteration: {iterations}")

x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)

X, Y = np.meshgrid(x, y)
Z1 = np.sin(X + 0.5) - Y - 1
Z2 = np.cos(Y - 2) + X

plt.contour(X, Y, Z1, levels=[0], colors='r')
plt.contour(X, Y, Z2, levels=[0], colors='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графічне відображення системи рівнянь')
plt.grid(True)
plt.show()
