# Bước 1: Khởi tạo từ điển với một vài từ mẫu
tu_dien = {
    "hello": "xin chào",
    "world": "thế giới",
    "cat": "con mèo"
}

# Bước 2: Bắt đầu vòng lặp chính của chương trình
while True:
    # In ra menu cho người dùng lựa chọn
    print("\n----- TỪ ĐIỂN ANH-VIỆT -----")
    print("1. Xem toàn bộ từ vựng")
    print("2. Thêm từ mới")
    print("3. Tra từ")
    print("4. Xóa từ")
    print("5. Thoát")

    # Lấy lựa chọn từ người dùng
    try:
        lua_chon = int(input("Nhập lựa chọn của bạn (1-5): "))
    except ValueError:
        print("Lựa chọn không hợp lệ. Vui lòng nhập một số.")
        continue  # Quay lại đầu vòng lặp

    # Bước 3: Xử lý các lựa chọn bằng if/elif/else

    # Chức năng 1: Xem toàn bộ từ vựng
    if lua_chon == 1:
        print("\n--- Toàn bộ từ vựng ---")
        if not tu_dien:
            print("Từ điển đang trống.")
        else:
            for tu_tieng_anh, nghia_tieng_viet in tu_dien.items():
                print(f"- {tu_tieng_anh}: {nghia_tieng_viet}")

    # Chức năng 2: Thêm từ mới
    elif lua_chon == 2:
        tu_moi = input("Nhập từ tiếng Anh mới: ").lower()
        nghia_moi = input(f"Nhập nghĩa của '{tu_moi}': ")
        tu_dien[tu_moi] = nghia_moi
        print(f"Đã thêm từ '{tu_moi}' thành công!")

    # Chức năng 3: Tra từ
    elif lua_chon == 3:
        tu_can_tra = input("Nhập từ tiếng Anh cần tra: ").lower()
        if tu_can_tra in tu_dien:
            print(f"-> Nghĩa của '{tu_can_tra}' là: {tu_dien[tu_can_tra]}")
        else:
            print(f"Không tìm thấy từ '{tu_can_tra}' trong từ điển.")

    # Chức năng 4: Xóa từ
    elif lua_chon == 4:
        tu_can_xoa = input("Nhập từ tiếng Anh cần xóa: ").lower()
        if tu_can_xoa in tu_dien:
            del tu_dien[tu_can_xoa]
            print(f"Đã xóa từ '{tu_can_xoa}' thành công!")
        else:
            print(f"Không tìm thấy từ '{tu_can_xoa}' để xóa.")

    # Chức năng 5: Thoát
    elif lua_chon == 5:
        print("Cảm ơn đã sử dụng từ điển. Tạm biệt!")
        break  # Phá vỡ vòng lặp while True để kết thúc chương trình

    # Xử lý lựa chọn không hợp lệ
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")