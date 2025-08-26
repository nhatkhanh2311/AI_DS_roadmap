import numpy as np

# Ma trận A và kết quả đã tính từ bài học
A = np.array([[4, 2],
              [1, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)

# 1. Lấy trị riêng và vector riêng đầu tiên
lambda1 = eigenvalues[0]
v1 = eigenvectors[:, 0] # Lấy cột đầu tiên

print("--- Bài 1: Kiểm chứng Phương trình Eigen ---")
print(f"Trị riêng λ1 = {lambda1}")
print(f"Vector riêng v1 = {v1}")

# 2. Tính vế trái: A @ v1
left_side = A @ v1
print(f"\nVế trái (A @ v1) = {left_side}")

# 3. Tính vế phải: λ1 * v1
right_side = lambda1 * v1
print(f"Vế phải (λ1 * v1) = {right_side}")

# 4. Kiểm tra sự bằng nhau
# Dùng np.allclose để so sánh hai array số thực một cách an toàn
are_equal = np.allclose(left_side, right_side)
print(f"\nHai vế có bằng nhau không? {are_equal}")
