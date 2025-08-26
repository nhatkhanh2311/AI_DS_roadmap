import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces

# Bước 1: Load ảnh
faces = fetch_olivetti_faces()
image = faces.images[0]  # Lấy ảnh đầu tiên, kích thước (64, 64)

# Bước 2: Thực hiện SVD
U, S, VT = np.linalg.svd(image)

# Bước 3 & 4: Nén và Tái tạo với các giá trị k khác nhau
plt.figure(figsize=(15, 5))

# Hiển thị ảnh gốc
plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title(f"Ảnh Gốc\n(Rank={np.linalg.matrix_rank(image)})")
plt.axis('off')

k_values = [5, 15, 30]
for i, k in enumerate(k_values):
    # Tái tạo lại ma trận Sigma chỉ với k giá trị suy biến
    Sigma_k = np.zeros(image.shape)
    Sigma_k[:k, :k] = np.diag(S[:k])

    # Tái tạo ảnh
    reconstructed_image = U @ Sigma_k @ VT

    # Hiển thị ảnh đã nén
    plt.subplot(1, 4, i + 2)
    plt.imshow(reconstructed_image, cmap='gray')
    plt.title(f"Ảnh Tái tạo\n(k = {k})")
    plt.axis('off')

plt.tight_layout()
plt.show()
