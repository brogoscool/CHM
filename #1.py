import math

# Функція для порівняння точності двох рівностей
def compare_accuracy():
    # Обчислюємо значення √18
    sqrt_18 = math.sqrt(18)

    # Обчислюємо значення 9/11
    nine_eleven = 9/11

    # Визначаємо, яка рівність точніша
    if abs(sqrt_18 - 4.24) < abs(nine_eleven - 0.818):
        return "√18 ≈ 4.24 є точнішою."
    else:
        return "9/11 ≈ 0.818 є точнішою."

# Викликаємо функцію та виводимо результат
result = compare_accuracy()
print(result)
