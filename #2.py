def equation(x):
    return (4.5 * x**4) - (4 * x**3) + (1.5 * x**2) - 2 * x - 7

def bisection_method(f, a, b, tol):
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

def chord_method(f, a, b, tol):
    while abs(a - b) > tol:
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(x)) < tol:
            return x
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x
    return (a + b) / 2.0


a = 0
b = 1
tolerance = 0.0001

root_bisection = bisection_method(equation, a, b, tolerance)
root_chord = chord_method(equation, a, b, tolerance)

print(f"Корінь, знайдений методом половинного ділення: {root_bisection:.4f}")
print(f"Корінь, знайдений методом хорд: {root_chord:.4f}")
