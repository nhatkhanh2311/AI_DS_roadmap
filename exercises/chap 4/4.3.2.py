import pandas as pd
from sklearn.model_selection import train_test_split

# --- Bài 2: Kỹ thuật Đặc trưng Thủ công (Code độc lập) ---
print("--- Bài 2: Trích xuất Chức danh ---")

try:
    # 1. Tải và chuẩn bị dữ liệu từ đầu
    df_original = pd.read_csv('titanic.csv')
    X = df_original.drop('Survived', axis=1)
    y = df_original['Survived']

    # 2. Tạo ra các tập X_train, X_test riêng cho bài tập này
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )


    # 3. Định nghĩa hàm trích xuất chức danh
    def extract_title(name):
        """
        Trích xuất chức danh (Mr, Mrs, Miss, etc.) từ cột Name.
        """
        part2 = name.split(',')[1]
        title = part2.split('.')[0]
        return title.strip()


    # 4. Áp dụng hàm để tạo cột 'Title' mới
    # Dùng .copy() để đảm bảo chúng ta không làm việc trên một lát cắt, tránh cảnh báo
    X_train_copy = X_train.copy()
    X_test_copy = X_test.copy()
    X_train_copy['Title'] = X_train_copy['Name'].apply(extract_title)
    X_test_copy['Title'] = X_test_copy['Name'].apply(extract_title)

    # 5. In ra các chức danh và số lượng của chúng trong tập train
    print("Các chức danh và số lượng trong tập train:")
    print(X_train_copy['Title'].value_counts())

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'. Vui lòng đảm bảo file đã được tải.")
