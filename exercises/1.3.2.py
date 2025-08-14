import math  # Import thư viện math để dùng hàm căn bậc hai


def is_prime(number):
    """
    Kiểm tra xem một số có phải là số nguyên tố hay không.
    Trả về True nếu là số nguyên tố, ngược lại trả về False.
    """
    # Số nguyên tố phải lớn hơn 1
    if number < 2:
        return False

    # Duyệt qua các số từ 2 cho đến căn bậc hai của number.
    # Nếu number chia hết cho bất kỳ số nào trong khoảng này, nó không phải là số nguyên tố.
    # Ta chỉ cần kiểm tra đến căn bậc hai vì nếu có một ước số lớn hơn căn bậc hai,
    # thì phải có một ước số tương ứng nhỏ hơn căn bậc hai.
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False  # Tìm thấy một ước số, nên nó không phải số nguyên tố

    # Nếu vòng lặp kết thúc mà không tìm thấy ước số nào, nó là số nguyên tố
    return True


def count_primes_in_list(numbers):
    """
    Đếm số lượng số nguyên tố trong một danh sách cho trước.
    """
    prime_count = 0
    for num in numbers:
        # Gọi hàm is_prime() để kiểm tra cho từng số
        if is_prime(num):
            prime_count += 1
    return prime_count


# Ví dụ sử dụng
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 20]
number_of_primes = count_primes_in_list(my_list)

print("\n--- Đếm số nguyên tố ---")
print(f"Danh sách ban đầu: {my_list}")
print(
    f"Số lượng số nguyên tố trong danh sách là: {number_of_primes}")  # Output: 8 (là các số 2, 3, 5, 7, 11, 13, 17, 19)
