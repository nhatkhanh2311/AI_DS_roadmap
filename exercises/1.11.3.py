def sorted_squares_simple(nums):
    """
    Cách 1 (Đơn giản): Bình phương rồi sắp xếp.
    Độ phức tạp: O(n) cho việc bình phương + O(n log n) cho việc sắp xếp = O(n log n)
    """
    squares = [num * num for num in nums]
    squares.sort()
    return squares


def sorted_squares_two_pointers(nums):
    """
    Cách 2 (Tối ưu): Dùng hai con trỏ.
    Độ phức tạp: O(n)
    """
    n = len(nums)
    result = [0] * n  # Tạo một danh sách kết quả rỗng có cùng kích thước
    left = 0
    right = n - 1

    # Điền vào danh sách kết quả từ cuối về đầu
    for i in range(n - 1, -1, -1):
        # So sánh giá trị tuyệt đối của hai phần tử ở hai đầu
        if abs(nums[left]) > abs(nums[right]):
            square = nums[left] ** 2
            left += 1
        else:
            square = nums[right] ** 2
            right -= 1
        result[i] = square

    return result


# Ví dụ sử dụng
nums = [-4, -1, 0, 3, 10]

print("\n--- Bình phương và Sắp xếp ---")
print(f"Danh sách gốc: {nums}")
print(f"Cách 1 (đơn giản): {sorted_squares_simple(nums.copy())}")
print(f"Cách 2 (hai con trỏ): {sorted_squares_two_pointers(nums.copy())}")
