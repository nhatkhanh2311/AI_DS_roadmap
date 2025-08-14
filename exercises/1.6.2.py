# Khởi tạo các biến đếm
line_count = 0
word_count = 0

print("\n--- Phân tích file my_diary.txt ---")

try:
    # Mở file my_diary.txt ở chế độ 'r' (read)
    with open('my_diary.txt', 'r', encoding='utf-8') as f:
        # Dùng vòng lặp for để đọc từng dòng
        for line in f:
            # 1. Mỗi lần lặp qua một dòng, tăng biến đếm dòng lên 1
            line_count += 1

            # 2. Tách dòng thành một danh sách các từ
            words_in_line = line.split()

            # 3. Cộng số lượng từ trong dòng này vào tổng số từ
            word_count += len(words_in_line)

    # In kết quả cuối cùng
    print(f"Tổng số dòng trong file là: {line_count}")
    print(f"Tổng số từ trong file là: {word_count}")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'my_diary.txt'. Vui lòng chạy bài tập 1 trước.")
