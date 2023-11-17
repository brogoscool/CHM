import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial

x = sp.symbols("x")

f = sp.exp(sp.sin(5 * x))

f_prime_1 = sp.diff(f, x)
f_prime_2 = sp.diff(f_prime_1, x)
f_prime_3 = sp.diff(f_prime_2, x)

x_val = 0
f_val = f.subs(x, x_val)
f_prime_1_val = f_prime_1.subs(x, x_val)
f_prime_2_val = f_prime_2.subs(x, x_val)
f_prime_3_val = f_prime_3.subs(x, x_val)

taylor_approximation = sp.series(f, x, x_val, 4).removeO()

error = sp.Abs(f - taylor_approximation).subs(x, x_val)

print("Функція:", f)
print("Перша похідна:", f_prime_1)
print("Друга похідна:", f_prime_2)
print("Третя похідна:", f_prime_3)
print("\nЗначення в точці x=0:")
print("Функція:", f_val)
print("Перша похідна:", f_prime_1_val)
print("Друга похідна:", f_prime_2_val)
print("Третя похідна:", f_prime_3_val)
print("\nМногочлен Тейлора (за 4-м ступенем):", taylor_approximation)
print("Похибка:", error)

x_range = np.linspace(-1, 1, 100)
f_np = sp.lambdify(x, f, "numpy")
taylor_np = sp.lambdify(x, taylor_approximation, "numpy")

plt.plot(x_range, f_np(x_range), label="Функція")
plt.plot(x_range, taylor_np(x_range), label="Многочлен Тейлора (ступінь 4)")
plt.scatter([x_val], [f_val], color="red", label="Точка x=0")
plt.legend()
plt.title("Графік функції та наближення")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
