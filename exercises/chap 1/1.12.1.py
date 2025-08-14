# Dùng một dictionary làm cache để lưu kết quả đã tính
memo_cache = {}


def climb_stairs_memo(n):
    """
    Giải bài toán leo cầu thang bằng đệ quy có ghi nhớ.
    """
    # Nếu kết quả đã có trong cache, trả về luôn
    if n in memo_cache:
        return memo_cache[n]

    # Các trường hợp cơ sở
    if n == 0:
        result = 1  # Có 1 cách để ở bậc 0 (là không leo bước nào)
    elif n < 0:
        result = 0  # Không có cách nào để leo đến bậc âm
    else:
        # Bước đệ quy
        result = climb_stairs_memo(n - 1) + climb_stairs_memo(n - 2)

    # Lưu kết quả vào cache trước khi trả về
    memo_cache[n] = result
    return result


# Ví dụ
print("--- Dùng Memoization ---")
print(f"Số cách để leo 5 bậc cầu thang: {climb_stairs_memo(5)}")
print(f"Số cách để leo 10 bậc cầu thang: {climb_stairs_memo(10)}")
