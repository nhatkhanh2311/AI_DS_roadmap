import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

# --- 1. Chuẩn bị dữ liệu (Tương tự các bài trước) ---
try:
    df = pd.read_csv('titanic.csv')
    # Xử lý dữ liệu cơ bản
    df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    df.dropna(inplace=True)

    X = df.drop('Survived', axis=1)
    y = df['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Tiền xử lý với ColumnTransformer
    numeric_features = ['Age', 'Fare', 'SibSp', 'Parch']
    categorical_features = ['Pclass', 'Sex', 'Embarked']
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(), categorical_features)
        ])

    # Lưu ý: GaussianNB có thể xử lý trực tiếp các đặc trưng số,
    # nhưng việc chuẩn hóa (StandardScaler) không ảnh hưởng xấu đến nó.
    # OneHotEncoder là cần thiết cho các biến hạng mục.
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    print("Dữ liệu đã sẵn sàng, bắt đầu huấn luyện Gaussian Naive Bayes...")

    # --- 2. Huấn luyện mô hình GaussianNB ---
    gnb_model = GaussianNB()
    gnb_model.fit(X_train_processed, y_train)

    # --- 3. Đánh giá mô hình ---
    y_pred_gnb = gnb_model.predict(X_test_processed)

    print("\n--- Kết quả Đánh giá Mô hình Gaussian Naive Bayes ---")
    print(classification_report(y_test, y_pred_gnb))

    """
    So sánh với Logistic Regression (kết quả tham khảo từ bài 4.5):
    - Logistic Regression thường có F1-score cho lớp 1 (Sống sót) khoảng 0.75.
    - Gaussian Naive Bayes thường cho kết quả thấp hơn một chút trên bộ dữ liệu này,
      với F1-score cho lớp 1 có thể chỉ đạt khoảng 0.70 - 0.72.

    Lý do: Giả định "ngây thơ" về sự độc lập của các đặc trưng có thể không hoàn toàn đúng 
    với bộ dữ liệu Titanic. Ví dụ, 'Pclass' và 'Fare' rõ ràng là có liên quan đến nhau.
    Các mô hình như Logistic Regression có khả năng nắm bắt các mối tương quan này tốt hơn.

    => Kết luận: Trong trường hợp này, Logistic Regression là mô hình hoạt động hiệu quả hơn.
    """

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'.")
