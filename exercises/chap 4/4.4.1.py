import pandas as pd

print("--- Bài 1: Tạo đặc trưng tương tác Age_Pclass ---")

try:
    # Tải dữ liệu và xử lý giá trị thiếu cho cột Age
    df = pd.read_csv('titanic.csv')
    df['Age'] = df['Age'].fillna(df['Age'].median())

    # Tạo đặc trưng tương tác Age_Pclass
    df['Age_Pclass'] = df['Age'] * df['Pclass']

    # In ra 5 dòng đầu của các cột liên quan để xem kết quả
    print(df[['Age', 'Pclass', 'Age_Pclass']].head())

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'.")
