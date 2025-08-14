def fizzbuzz(n):
    """
    In ra các số từ 1 đến n theo quy tắc FizzBuzz.
    """
    # Sử dụng vòng lặp for và hàm range() để duyệt qua các số từ 1 đến n
    for i in range(1, n + 1):
        # Điều kiện quan trọng nhất (chia hết cho cả 3 và 5) phải được kiểm tra đầu tiên.
        # Nếu không, chương trình sẽ lọt vào if (i % 3 == 0) và không bao giờ xét đến trường hợp này.
        if i % 15 == 0:  # Hoặc (i % 3 == 0) and (i % 5 == 0)
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Ví dụ gọi hàm với n = 20
print("--- Chạy FizzBuzz với n = 20 ---")
fizzbuzz(20)
