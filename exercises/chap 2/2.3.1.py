import numpy as np

# Ma trận hệ số A
# Mỗi hàng tương ứng với một phương trình
# Mỗi cột tương ứng với hệ số của x, y, z
A = np.array([
    [1, 2, 1],
    [0, 2, -5],
    [2, 5, -1]
])

# Vector kết quả b
b = np.array([6, -4, 27])

print("--- Bài 1: Ma trận A và b ---")
print("Ma trận A:\n", A)
print("\nVector b:\n", b)
