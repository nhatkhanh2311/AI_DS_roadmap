import numpy as np

# Số lượng các mặt hàng
quantities = np.array([2, 1, 5]) # 2 bánh mì, 1 sữa, 5 trứng

# Giá tương ứng của mỗi mặt hàng
prices = np.array([15000, 25000, 3000]) # Giá bánh mì, sữa, trứng

# Sử dụng tích vô hướng để tính tổng tiền
# (2 * 15000) + (1 * 25000) + (5 * 3000)
total_cost = quantities @ prices # hoặc np.dot(quantities, prices)

print("\n--- Bài 3: Tính tiền Giỏ hàng ---")
print(f"Số lượng: {quantities}")
print(f"Đơn giá: {prices}")
print(f"Tổng tiền của giỏ hàng là: {total_cost} VND")
