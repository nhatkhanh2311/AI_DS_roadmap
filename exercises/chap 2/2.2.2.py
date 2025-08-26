import numpy as np
import matplotlib.pyplot as plt

# 1. Vector gốc
v = np.array([2, 1])

# 2. Ma trận biến đổi T
#    - Lật qua trục y (x -> -x)
#    - Tăng chiều cao gấp rưỡi (y -> 1.5*y)
T = np.array([[-1, 0],
              [0, 1.5]])

# 3. Áp dụng phép biến đổi
v_transformed = T @ v

# 4. Vẽ đồ thị
plt.figure(figsize=(6, 6))
# Vẽ vector gốc
plt.quiver(0, 0, v[0], v[1],
           angles='xy', scale_units='xy', scale=1, color='blue', label='Vector gốc [2, 1]')
# Vẽ vector đã biến đổi
plt.quiver(0, 0, v_transformed[0], v_transformed[1],
           angles='xy', scale_units='xy', scale=1, color='red', label=f'Vector biến đổi [{v_transformed[0]}, {v_transformed[1]}]')

# Cài đặt đồ thị
plt.xlim(-3, 3)
plt.ylim(-1, 3)
plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.title("Phép biến đổi Lật và Co giãn")
plt.show()
