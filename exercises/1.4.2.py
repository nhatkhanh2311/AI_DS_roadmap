def get_student_info():
    """
    Hàm này trả về thông tin cố định của một sinh viên dưới dạng tuple.
    """
    return "An", 22, "Hanoi"

# Gọi hàm để nhận tuple kết quả
student_data = get_student_info()

# Sử dụng kỹ thuật "unpacking" để gán các phần tử của tuple vào các biến riêng biệt
# Số lượng biến bên trái phải bằng số lượng phần tử trong tuple
name, age, city = student_data

# In các biến đã được gán
print(f"Tên: {name}")
print(f"Tuổi: {age}")
print(f"Thành phố: {city}")

# Việc cố gắng thay đổi tuple sẽ gây lỗi, ví dụ:
# student_data[1] = 23 # Dòng này sẽ báo TypeError
