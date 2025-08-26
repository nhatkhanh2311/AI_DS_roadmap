import numpy as np

# Ma trận M có cột 3 = cột 1 + cột 2
M = np.array([
    [1, 2, 3],
    [4, 5, 9],
    [6, 7, 13]
])

# Ma trận N là ma trận đơn vị (các cột độc lập tuyến tính)
N = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Tính hạng của hai ma trận
rank_M = np.linalg.matrix_rank(M)
rank_N = np.linalg.matrix_rank(N)

print("\n--- Bài 3: Hạng của Ma trận ---")
print(f"Hạng của ma trận M: {rank_M}")
print(f"Hạng của ma trận N: {rank_N}")
