import numpy as np

X = np.array([[1, 2],
              [3, 4]])

Y = np.array([[2, 0],
              [1, 2]])

Z = X @ Y

print("--- Kết quả tính bằng NumPy ---")
print(Z)
