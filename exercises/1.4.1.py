# Cho một danh sách ban đầu
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sử dụng List Comprehension để tạo list mới
# Cú pháp: [bieu_thuc for item in list if dieu_kien]
# 1. Lặp qua từng 'num' trong 'numbers'
# 2. Kiểm tra điều kiện 'if num % 2 == 0' (số chẵn)
# 3. Nếu đúng, tính 'num ** 2' (bình phương) và thêm vào list mới
even_squares = [num ** 2 for num in numbers if num % 2 == 0]

print(f"Danh sách gốc: {numbers}")
print(f"Bình phương của các số chẵn: {even_squares}")
