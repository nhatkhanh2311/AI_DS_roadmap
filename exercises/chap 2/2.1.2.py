import numpy as np

# Doanh số ban đầu của 2 cửa hàng
store1_sales = np.array([10, 20, 15, 25, 30])
store2_sales = np.array([5, 22, 18, 20, 28])

# 1. Tính tổng doanh số của cả hai cửa hàng theo từng ngày
total_sales = store1_sales + store2_sales

print("--- Bài 2: Phân tích Doanh số ---")
print(f"Doanh số cửa hàng 1: {store1_sales}")
print(f"Doanh số cửa hàng 2: {store2_sales}")
print(f"Tổng doanh số mỗi ngày: {total_sales}")

# 2. Tính doanh số mới của cửa hàng 1 sau khi tăng 20% (nhân với 1.2)
new_store1_sales = store1_sales * 1.2

print(f"Doanh số mới dự kiến của cửa hàng 1: {new_store1_sales}")
