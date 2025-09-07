import pandas as pd
from sklearn.model_selection import train_test_split

# --- Chuẩn bị Dữ liệu ---
# Các bước này giống như trong bài học để có được các tập dữ liệu ban đầu
try:
    df = pd.read_csv('titanic.csv')
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Điền giá trị thiếu cho cột Age như đã làm
    median_age = X_train['Age'].median()
    X_train['Age'] = X_train['Age'].fillna(median_age)
    X_test['Age'] = X_test['Age'].fillna(median_age)
    print("Dữ liệu đã được chuẩn bị, bắt đầu giải bài tập...\n")

    # --- Bài 1: Phân tích và Xử lý Cột `Embarked` ---
    print("--- Bài 1: Xử lý cột Embarked ---")

    # Kiểm tra số lượng giá trị thiếu ban đầu
    print(f"Số giá trị thiếu trong 'Embarked' (train set): {X_train['Embarked'].isnull().sum()}")

    # Tìm giá trị mode (giá trị xuất hiện nhiều nhất) của cột Embarked trên tập train
    embarked_mode = X_train['Embarked'].mode()[0]
    print(f"Giá trị phổ biến nhất (mode) của 'Embarked' là: '{embarked_mode}'")

    # Điền các giá trị thiếu bằng giá trị mode vừa tìm được
    X_train['Embarked'] = X_train['Embarked'].fillna(embarked_mode)
    X_test['Embarked'] = X_test['Embarked'].fillna(embarked_mode)

    print(f"Số giá trị thiếu trong 'Embarked' sau khi xử lý: {X_train['Embarked'].isnull().sum()}")

    # --- Bài 2: Phân tích và Xử lý Cột `Cabin` ---
    print("\n--- Bài 2: Xử lý cột Cabin ---")

    # Kiểm tra số lượng giá trị thiếu
    missing_cabin = X_train['Cabin'].isnull().sum()
    total_cabin = len(X_train['Cabin'])
    missing_percentage = (missing_cabin / total_cabin) * 100

    print(f"Số giá trị thiếu trong 'Cabin': {missing_cabin} trên tổng số {total_cabin} ({missing_percentage:.2f}%)")

    """
    Nhận xét:
    Cột 'Cabin' thiếu tới hơn 77% dữ liệu. Việc cố gắng điền các giá trị này 
    sẽ không đáng tin cậy và có thể đưa thông tin sai lệch vào mô hình.
    Do đó, chiến lược hợp lý nhất trong trường hợp này là xóa bỏ hoàn toàn cột này.
    """

    # Xóa cột 'Cabin' khỏi cả hai tập dữ liệu
    # axis=1: chỉ định rằng chúng ta đang xóa một cột
    X_train.drop('Cabin', axis=1, inplace=True)
    X_test.drop('Cabin', axis=1, inplace=True)

    print("Đã xóa cột 'Cabin' khỏi X_train và X_test.")

    print("\nKiểm tra lại các giá trị thiếu trong X_train sau khi xử lý:")
    print(X_train.isnull().sum())


except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'. Vui lòng đảm bảo file đã được tải và đặt đúng thư mục.")
