from sympy import symbols, diff

# Khai báo các biến
x, y = symbols('x y')

# Định nghĩa hàm số
f = x**3 - 4*x**2*y + 5*y**2

# Tính đạo hàm riêng
df_dx = diff(f, x)
df_dy = diff(f, y)

print("--- Kiểm tra với SymPy ---")
print(f"Hàm số f(x, y) = {f}")
print(f"Đạo hàm riêng theo x: {df_dx}")
print(f"Đạo hàm riêng theo y: {df_dy}")
