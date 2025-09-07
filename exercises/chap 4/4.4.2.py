import pandas as pd

print("\n--- Bài 2: Phân tích và gom nhóm đặc trưng Title ---")

try:
    # Tải dữ liệu
    df = pd.read_csv('titanic.csv')

    # 1. Định nghĩa hàm trích xuất chức danh
    def extract_title(name):
        return name.split(',')[1].split('.')[0].strip()

    # 2. Tạo cột 'Title'
    df['Title'] = df['Name'].apply(extract_title)

    # 3. Gom nhóm các chức danh hiếm
    common_titles = ['Mr', 'Miss', 'Mrs', 'Master']
    df['Title'] = df['Title'].apply(lambda title: title if title in common_titles else 'Other')

    print("Tần suất các chức danh sau khi gom nhóm:")
    print(df['Title'].value_counts())

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'.")
