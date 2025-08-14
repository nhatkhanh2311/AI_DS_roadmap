def climb_stairs_tab(n):
    """
    Giải bài toán leo cầu thang bằng phương pháp bảng.
    """
    # Xử lý các trường hợp cơ sở
    if n == 0:
        return 1
    if n == 1:
        return 1

    # Tạo một bảng để lưu số cách đến từng bậc
    # dp_table[i] sẽ là số cách để đến được bậc thứ i
    dp_table = [0] * (n + 1)

    # Điền vào các giá trị cơ sở
    dp_table[0] = 1
    dp_table[1] = 1

    # Tuần tự điền vào bảng từ bậc 2 đến n
    for i in range(2, n + 1):
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

    return dp_table[n]


# Ví dụ
print("\n--- Dùng Tabulation ---")
print(f"Số cách để leo 5 bậc cầu thang: {climb_stairs_tab(5)}")
print(f"Số cách để leo 10 bậc cầu thang: {climb_stairs_tab(10)}")
