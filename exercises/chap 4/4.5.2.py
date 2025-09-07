import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

try:
    # --- 1. Chuẩn bị dữ liệu (Tương tự bài học) ---
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

    # --- 2. Huấn luyện và Đánh giá RandomForestClassifier ---
    print("--- Kết quả của RandomForestClassifier ---")

    # a. Khởi tạo và huấn luyện mô hình
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train_processed, y_train)

    # b. Đưa ra dự đoán
    y_pred_rf = rf_model.predict(X_test_processed)

    # c. In ra Classification Report
    print("Classification Report:")
    print(classification_report(y_test, y_pred_rf))

    # d. Vẽ Ma trận Nhầm lẫn
    cm_rf = confusion_matrix(y_test, y_pred_rf)
    disp_rf = ConfusionMatrixDisplay(confusion_matrix=cm_rf)
    disp_rf.plot()
    plt.title("Ma trận Nhầm lẫn - Random Forest")
    plt.show()

    """
    So sánh với Logistic Regression (kết quả từ bài học):
    - Logistic Regression thường có F1-score cho lớp 1 (Sống sót) khoảng 0.75.
    - RandomForestClassifier thường cho kết quả tốt hơn đáng kể, với F1-score cho lớp 1 có thể đạt khoảng 0.78 - 0.80.
    - Nhìn vào Ma trận nhầm lẫn, bạn sẽ thấy RandomForest thường dự đoán đúng nhiều True Positive và True Negative hơn.

    => Kết luận: Trong trường hợp này, RandomForestClassifier là mô hình hoạt động tốt hơn.
    """

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'.")
