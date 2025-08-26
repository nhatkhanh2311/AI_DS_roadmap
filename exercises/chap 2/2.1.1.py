import numpy as np

# 1. Tạo một array 1D chứa các số từ 1 đến 12
initial_array = np.arange(1, 13)

# 2. Dùng phương thức .reshape() để đổi nó thành ma trận 3x4
A = initial_array.reshape(3, 4)

# 3. In ra ma trận và các thuộc tính của nó
print("--- Bài 1: Ma trận A ---")
print(A)
print(f"Shape: {A.shape}")   # (3, 4) -> 3 hàng, 4 cột
print(f"Ndim (số chiều): {A.ndim}") # 2
print(f"Size (tổng số phần tử): {A.size}") # 12
