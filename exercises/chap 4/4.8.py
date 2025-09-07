import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression

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
    X_train_processed = preprocessor.fit_transform(X_train)

    print("Dữ liệu đã sẵn sàng, bắt đầu Grid Search...")

    # --- 2. Tạo lưới Siêu tham số ---
    param_grid = {
        'penalty': ['l1', 'l2'],
        'C': [0.01, 0.1, 1, 10, 100]
    }

    # --- 3. Khởi tạo và Chạy Grid Search ---
    # Sử dụng solver='liblinear' vì nó hỗ trợ cả penalty 'l1' và 'l2'
    log_reg = LogisticRegression(solver='liblinear', random_state=42)

    grid_search = GridSearchCV(
        estimator=log_reg,
        param_grid=param_grid,
        cv=5,  # 5-fold cross-validation
        scoring='accuracy',
        n_jobs=-1  # Sử dụng tất cả các nhân CPU
    )

    # Huấn luyện (quá trình này có thể mất một chút thời gian)
    grid_search.fit(X_train_processed, y_train)

    # --- 4. In kết quả ---
    print("\n--- Kết quả Grid Search cho LogisticRegression ---")
    print(f"Bộ siêu tham số tốt nhất tìm được: {grid_search.best_params_}")
    print(f"Accuracy tốt nhất trên tập validation (cross-validation): {grid_search.best_score_:.4f}")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'.")
