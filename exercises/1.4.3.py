from collections import namedtuple

# 1. Định nghĩa một "khuôn mẫu" namedtuple tên là 'Color'
# Nó sẽ có 3 trường (fields) là 'R', 'G', và 'B'.
Color = namedtuple("Color", ["R", "G", "B"])

# 2. Tạo một đối tượng (instance) từ khuôn mẫu Color
# Dữ liệu được truyền vào như các đối số thông thường.
red_color = Color(R=255, G=0, B=0)

# 3. Truy cập các trường dữ liệu bằng tên, giúp code dễ đọc hơn nhiều
print(f"Đối tượng màu đỏ: {red_color}")
print(f"Giá trị Green của màu đỏ là: {red_color.G}")
