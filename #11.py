import numpy as np
from scipy import integrate


#! МЕТОД ПРЯМОКУТНИКІВ
def rectangle_method(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    integral = h * np.sum(y[:-1])
    return integral


func1 = lambda x: 1 / np.sqrt(2 * x + 3)
a1 = 0.8
b1 = 1.4
n1 = 10
result1 = rectangle_method(func1, a1, b1, n1)
print(f"Значення інтегралу методом прямокутників (функція 1): {result1:.4f}")

func2 = lambda x: np.sqrt(x) * np.cos(x**2)
a2 = 0.4
b2 = 1.2
n2 = 10
result2 = rectangle_method(func2, a2, b2, n2)
print(f"Значення інтегралу методом прямокутників (функція 2): {result2:.4f}")

func3 = lambda x: 1 / np.sqrt(3 * x**2 - 0.4)
a3 = 1.3
b3 = 2.1
n3 = 10
result3 = rectangle_method(func3, a3, b3, n3)
print(f"Значення інтегралу методом прямокутників (функція 3): {result3:.4f}")






#! МЕТОД СІМПСОНА

result1_simpson = integrate.simpson(
    func1(np.linspace(a1, b1, n1 + 1)), np.linspace(a1, b1, n1 + 1)
)
print(f"Значення інтегралу методом Сімпсона (функція 1): {result1_simpson:.4f}")

# Функція 2
result2_simpson = integrate.simpson(
    func2(np.linspace(a2, b2, n2 + 1)), np.linspace(a2, b2, n2 + 1)
)
print(f"Значення інтегралу методом Сімпсона (функція 2): {result2_simpson:.4f}")

# Функція 3
result3_simpson = integrate.simpson(
    func3(np.linspace(a3, b3, n3 + 1)), np.linspace(a3, b3, n3 + 1)
)
print(f"Значення інтегралу методом Сімпсона (функція 3): {result3_simpson:.4f}")






#! МЕТОД ТРАПЕЦІЙ

result1_trapezoidal = integrate.trapz(
    func1(np.linspace(a1, b1, n1 + 1)), np.linspace(a1, b1, n1 + 1)
)
print(f"Значення інтегралу методом трапецій (функція 1): {result1_trapezoidal:.4f}")

result2_trapezoidal = integrate.trapz(
    func2(np.linspace(a2, b2, n2 + 1)), np.linspace(a2, b2, n2 + 1)
)
print(f"Значення інтегралу методом трапецій (функція 2): {result2_trapezoidal:.4f}")

result3_trapezoidal = integrate.trapz(
    func3(np.linspace(a3, b3, n3 + 1)), np.linspace(a3, b3, n3 + 1)
)
print(f"Значення інтегралу методом трапецій (функція 3): {result3_trapezoidal:.4f}")
