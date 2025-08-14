# --- Lớp cha (Parent Class) ---
class Vehicle:
    """
    Lớp cha đại diện cho một phương tiện giao thông chung.
    """
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Hãng: {self.brand}")
        print(f"Năm sản xuất: {self.year}")

# --- Lớp con thứ nhất (Child Class) ---
class Car(Vehicle):
    """
    Lớp con Car kế thừa từ Vehicle.
    """
    def __init__(self, brand, year, door_count):
        # Gọi phương thức __init__ của lớp cha (Vehicle) để gán brand và year
        super().__init__(brand, year)
        # Thêm thuộc tính riêng của Car
        self.door_count = door_count

    def display_info(self):
        # Ghi đè phương thức: gọi phương thức của lớp cha trước
        print("--- Thông tin xe hơi ---")
        super().display_info()
        # In thêm thông tin riêng của lớp con
        print(f"Số cửa: {self.door_count}")

# --- Lớp con thứ hai (Child Class) ---
class Motorbike(Vehicle):
    """
    Lớp con Motorbike kế thừa từ Vehicle.
    """
    def __init__(self, brand, year, engine_cc):
        # Gọi phương thức __init__ của lớp cha (Vehicle)
        super().__init__(brand, year)
        # Thêm thuộc tính riêng của Motorbike
        self.engine_cc = engine_cc

    def display_info(self):
        # Ghi đè phương thức: gọi phương thức của lớp cha trước
        print("--- Thông tin xe máy ---")
        super().display_info()
        # In thêm thông tin riêng của lớp con
        print(f"Phân khối: {self.engine_cc}cc")


# --- Tạo và Sử dụng Đối tượng ---

# Tạo một đối tượng từ lớp Car
my_car = Car(brand="Toyota", year=2022, door_count=4)

# Tạo một đối tượng từ lớp Motorbike
my_motorbike = Motorbike(brand="Honda", year=2023, engine_cc=150)

# Gọi phương thức display_info() của cả hai đối tượng
# Đây là ví dụ về tính đa hình: cùng một tên phương thức nhưng hành vi khác nhau
my_car.display_info()
print("\n") # In một dòng trống để tách biệt
my_motorbike.display_info()
