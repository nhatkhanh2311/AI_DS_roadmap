import pandas as pd
from scipy.stats import ttest_ind

# --- Bài 1: Phát biểu Giả thuyết ---

print("--- Bài 1: Phát biểu Giả thuyết ---")
print("Bài toán: Kiểm tra sự khác biệt về tuổi trung bình giữa người sống sót và người tử vong.")
print("Giả thuyết không (H0): Tuổi trung bình của nhóm sống sót và nhóm tử vong là BẰNG NHAU.")
print("Giả thuyết đối (H1): Tuổi trung bình của nhóm sống sót và nhóm tử vong là KHÁC NHAU.")

# --- Bài 2: Thực hiện T-test ---

print("\n--- Bài 2: Thực hiện T-test ---")

try:
    # Đọc dữ liệu
    df = pd.read_csv('titanic.csv')

    # Tạo hai mẫu dữ liệu, loại bỏ các giá trị tuổi bị thiếu (.dropna())
    survived_age = df[df['Survived'] == 1]['Age'].dropna()
    deceased_age = df[df['Survived'] == 0]['Age'].dropna()

    # Thực hiện T-test để so sánh trung bình của hai mẫu độc lập
    t_statistic, p_value = ttest_ind(survived_age, deceased_age)

    print(f"P-value tính được từ T-test là: {p_value:.4f}")

    # --- Bài 3: Rút ra Kết luận ---
    print("\n--- Bài 3: Rút ra Kết luận ---")

    alpha = 0.05  # Mức ý nghĩa thông thường

    # So sánh p-value với mức ý nghĩa alpha
    if p_value < alpha:
        print(f"Vì p-value ({p_value:.4f}) < {alpha}, chúng ta BÁC BỎ giả thuyết không (H0).")
        print(
            "\n=> Kết luận: Có bằng chứng thống kê để nói rằng có sự khác biệt về tuổi trung bình giữa nhóm sống sót và nhóm tử vong.")
    else:
        print(f"Vì p-value ({p_value:.4f}) >= {alpha}, chúng ta KHÔNG ĐỦ BẰNG CHỨNG để bác bỏ giả thuyết không (H0).")
        print("\n=> Kết luận: Không có sự khác biệt có ý nghĩa thống kê về tuổi trung bình giữa hai nhóm.")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'. Vui lòng đảm bảo file đã được tải và đặt đúng thư mục.")

# Phân tích thêm (không bắt buộc):
# mean_survived = survived_age.mean()
# mean_deceased = deceased_age.mean()
# print(f"\nTuổi trung bình của người sống sót: {mean_survived:.2f}")
# print(f"Tuổi trung bình của người tử vong: {mean_deceased:.2f}")
# Chúng ta thấy tuổi trung bình của người sống sót (khoảng 28.34) thấp hơn một chút so với người tử vong (khoảng 30.63),
# và T-test đã xác nhận rằng sự khác biệt này có ý nghĩa thống kê (không phải do ngẫu nhiên).
