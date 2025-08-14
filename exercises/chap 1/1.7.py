class Rectangle:
    """
    Lớp này đại diện cho một hình chữ nhật.

    Thuộc tính:
        width (int, float): Chiều rộng của hình chữ nhật.
        height (int, float): Chiều cao của hình chữ nhật.
    """

    def __init__(self, width, height):
        """
        Phương thức khởi tạo cho một đối tượng Rectangle mới.
        """
        self.width = width
        self.height = height

    def calculate_area(self):
        """
        Tính và trả về diện tích của hình chữ nhật.
        """
        return self.width * self.height

    def calculate_perimeter(self):
        """
        Tính và trả về chu vi của hình chữ nhật.
        """
        return 2 * (self.width + self.height)

    def is_square(self):
        """
        Kiểm tra xem hình chữ nhật có phải là hình vuông hay không.
        Trả về True nếu là hình vuông, ngược lại trả về False.
        """
        return self.width == self.height


# --- Tạo và Sử dụng Đối tượng ---

# 1. Tạo đối tượng thứ nhất (hình chữ nhật)
rect1 = Rectangle(width=5, height=10)

print("--- Thông tin Hình chữ nhật 1 ---")
print(f"Chiều rộng: {rect1.width}, Chiều cao: {rect1.height}")
print(f"Diện tích: {rect1.calculate_area()}")
print(f"Chu vi: {rect1.calculate_perimeter()}")
print(f"Là hình vuông? {rect1.is_square()}")

# 2. Tạo đối tượng thứ hai (hình vuông)
rect2 = Rectangle(width=7, height=7)

print("\n--- Thông tin Hình chữ nhật 2 ---")
print(f"Chiều rộng: {rect2.width}, Chiều cao: {rect2.height}")
print(f"Diện tích: {rect2.calculate_area()}")
print(f"Chu vi: {rect2.calculate_perimeter()}")
print(f"Là hình vuông? {rect2.is_square()}")
