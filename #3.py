import numpy as np
np.random.seed(0)

N = 4
M = 5

A = np.random.randint(-10, 10, size=(N, M))

print("Матриця A:")
print(A)

column_sums = np.sum(np.abs(A), axis=0)
max_column_index = np.argmax(column_sums)

print(f"Стовпчастий елемент з максимальною сумою абсолютних значень знаходиться в стовпці {max_column_index}.")

max_sum = column_sums[max_column_index]
print(f"Максимальна сума абсолютних значень в стовпці: {max_sum}")
