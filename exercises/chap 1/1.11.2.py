def is_palindrome(s):
    """
    Kiểm tra chuỗi đối xứng bằng kỹ thuật hai con trỏ.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # So sánh ký tự ở hai đầu
        if s[left] != s[right]:
            return False  # Nếu chúng khác nhau, đây không phải chuỗi đối xứng

        # Di chuyển hai con trỏ vào trong
        left += 1
        right -= 1

    # Nếu vòng lặp kết thúc mà không tìm thấy sự khác biệt, nó là chuỗi đối xứng
    return True


# Ví dụ sử dụng
string1 = "racecar"
string2 = "hello"

print(f"\nChuỗi '{string1}' có phải đối xứng không? {is_palindrome(string1)}")
print(f"Chuỗi '{string2}' có phải đối xứng không? {is_palindrome(string2)}")
