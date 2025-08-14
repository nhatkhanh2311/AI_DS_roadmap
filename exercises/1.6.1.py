# --- Bước 1: Ghi đè file với chế độ 'w' ---

# Nội dung ban đầu
initial_lines = [
    "Ngày 13 tháng 8 năm 2025:\n",
    "Bắt đầu học về cách làm việc với file trong Python.\n"
]

# Mở file my_diary.txt ở chế độ 'w' (write)
# Nếu file tồn tại, nội dung cũ sẽ bị xóa
# Nếu file chưa tồn tại, nó sẽ được tạo mới
with open('my_diary.txt', 'w', encoding='utf-8') as f:
    f.writelines(initial_lines)

print("Đã ghi 2 dòng đầu tiên vào my_diary.txt.")

# --- Bước 2: Ghi nối vào file với chế độ 'a' ---

# Nội dung cần thêm
additional_line = "Khá thú vị và hữu ích!\n"

# Mở lại file my_diary.txt ở chế độ 'a' (append)
# Nội dung mới sẽ được thêm vào cuối file
with open('my_diary.txt', 'a', encoding='utf-8') as f:
    f.write(additional_line)

print("Đã ghi nối thêm 1 dòng vào my_diary.txt.")

# Bây giờ, bạn có thể mở file my_diary.txt trong VS Code để xem kết quả.
# Nội dung của nó sẽ là:
# Ngày 13 tháng 8 năm 2025:
# Bắt đầu học về cách làm việc với file trong Python.
# Khá thú vị và hữu ích!
