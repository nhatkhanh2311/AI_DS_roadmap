import numpy as np

# Lấy lại ma trận A và b từ bài 1
A = np.array([
    [1, 2, 1],
    [0, 2, -5],
    [2, 5, -1]
])
b = np.array([6, -4, 27])

# Sử dụng np.linalg.solve() để tìm nghiệm [x, y, z]
solution = np.linalg.solve(A, b)

print("\n--- Bài 2: Nghiệm của hệ phương trình ---")
print(f"Nghiệm (x, y, z) là: {solution}")

# Kiểm tra lại bằng cách nhân A với nghiệm, kết quả phải ra vector b
# print("\nKiểm tra lại A @ x:", A @ solution) # Sẽ ra [ 6. -4. 27.]
