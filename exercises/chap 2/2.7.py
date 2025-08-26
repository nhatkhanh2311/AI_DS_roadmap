import pandas as pd

# Giả sử file 'titanic.csv' đã có trong thư mục của bạn
try:
    df = pd.read_csv('titanic.csv')
    print("Đã đọc file titanic.csv thành công.")
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'. Vui lòng đảm bảo file đã được tải và đặt đúng thư mục.")
    df = None  # Gán df là None để code không chạy tiếp nếu có lỗi

# Chỉ chạy phần giải bài tập nếu dataframe được load thành công
if df is not None:
    # --- Bài 1: Lọc dữ liệu ---
    print("\n--- Bài 1: Lọc dữ liệu ---")

    # Tạo DataFrame mới chỉ chứa hành khách hạng nhất (Pclass == 1)
    class1_passengers = df[df['Pclass'] == 1]

    # Từ DataFrame trên, đếm số người đã sống sót (Survived == 1)
    # .sum() sẽ cộng tất cả các giá trị 1 lại
    num_survived_class1 = class1_passengers['Survived'].sum()

    print(f"Tổng số hành khách ở khoang hạng nhất: {len(class1_passengers)}")
    print(f"Số người sống sót ở khoang hạng nhất: {num_survived_class1}")

    # --- Bài 2: Tạo cột mới (Feature Engineering) ---
    print("\n--- Bài 2: Tạo cột mới ---")

    # Tạo cột 'FamilySize' bằng cách cộng 3 thành phần
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    # In ra 5 dòng đầu của DataFrame với cột mới
    # Chúng ta chọn các cột liên quan để xem cho rõ
    print(df[['Name', 'SibSp', 'Parch', 'FamilySize']].head())

    # --- Bài 3: Phân tích đơn giản ---
    print("\n--- Bài 3: Phân tích đơn giản ---")

    # Tạo điều kiện lọc
    alone_condition = df['FamilySize'] == 1
    family_condition = df['FamilySize'] > 1

    # Lọc và tính tỷ lệ sống sót (trung bình của cột Survived)
    survival_rate_alone = df[alone_condition]['Survived'].mean()
    survival_rate_family = df[family_condition]['Survived'].mean()

    # In kết quả, định dạng thành phần trăm
    print(f"Tỷ lệ sống sót của người đi một mình: {survival_rate_alone:.2%}")
    print(f"Tỷ lệ sống sót của người đi cùng gia đình: {survival_rate_family:.2%}")

    print("\nNhận xét: Hành khách đi cùng gia đình có tỷ lệ sống sót cao hơn đáng kể.")
