def find_unique_chars(input_string):
    """
    Hàm này nhận vào một chuỗi và trả về một set các ký tự duy nhất.
    """
    # 1. Chuyển toàn bộ chuỗi về chữ thường để không phân biệt hoa/thường
    lower_string = input_string.lower()

    # 2. Chuyển chuỗi đã xử lý thành một set.
    #    Set sẽ tự động loại bỏ các ký tự trùng lặp.
    unique_characters = set(lower_string)

    return unique_characters


# Ví dụ sử dụng
test_string = "Hello World"
unique_set = find_unique_chars(test_string)

print(f"Chuỗi gốc: '{test_string}'")
print(f"Các ký tự duy nhất: {unique_set}")
