import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# --- 1. Chuẩn bị dữ liệu ---
# Code này giả định bạn đã có các tập dữ liệu X_train, X_test, y_train, y_test
# và đối tượng preprocessor đã được 'fit' trên X_train.
# Để code chạy độc lập, chúng ta sẽ thực hiện lại các bước đó.
try:
    df = pd.read_csv('titanic.csv')
    df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    df.dropna(inplace=True)

    X = df.drop('Survived', axis=1)
    y = df['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    numeric_features = ['Age', 'Fare', 'SibSp', 'Parch']
    categorical_features = ['Pclass', 'Sex', 'Embarked']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(), categorical_features)
        ])

    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    print("Dữ liệu đã sẵn sàng, bắt đầu huấn luyện các mô hình SVM...")

    # --- 2. Huấn luyện và Đánh giá 3 mô hình SVM ---

    # a. SVM với Kernel Linear
    print("\n--- Kết quả SVM với Kernel 'linear' ---")
    svm_linear = SVC(kernel='linear', random_state=42)
    svm_linear.fit(X_train_processed, y_train)
    y_pred_linear = svm_linear.predict(X_test_processed)
    print(classification_report(y_test, y_pred_linear))

    # b. SVM với Kernel Poly
    print("\n--- Kết quả SVM với Kernel 'poly' ---")
    svm_poly = SVC(kernel='poly', random_state=42)
    svm_poly.fit(X_train_processed, y_train)
    y_pred_poly = svm_poly.predict(X_test_processed)
    print(classification_report(y_test, y_pred_poly))

    # c. SVM với Kernel RBF (mặc định)
    print("\n--- Kết quả SVM với Kernel 'rbf' ---")
    svm_rbf = SVC(kernel='rbf', random_state=42)
    svm_rbf.fit(X_train_processed, y_train)
    y_pred_rbf = svm_rbf.predict(X_test_processed)
    print(classification_report(y_test, y_pred_rbf))

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'.")
