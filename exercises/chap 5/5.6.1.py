import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# --- Chuẩn bị dữ liệu (tương tự bài học) ---
try:
    df = pd.read_csv('titanic.csv')
    df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
    df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

    # Sử dụng cách gán lại an toàn
    median_age = df['Age'].median()
    df['Age'] = df['Age'].fillna(median_age)

    df.dropna(inplace=True)
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- Huấn luyện cây không giới hạn độ sâu ---
    unlimited_tree = DecisionTreeClassifier(random_state=42)  # max_depth=None là mặc định
    unlimited_tree.fit(X_train, y_train)

    # --- Đánh giá ---
    # Dự đoán trên cả tập train và tập test
    y_pred_train = unlimited_tree.predict(X_train)
    y_pred_test = unlimited_tree.predict(X_test)

    # Tính accuracy
    accuracy_train = accuracy_score(y_train, y_pred_train)
    accuracy_test = accuracy_score(y_test, y_pred_test)

    print("--- Bài 1: Cây Bị Overfitting ---")
    print(f"Accuracy trên tập Train: {accuracy_train:.4f}")
    print(f"Accuracy trên tập Test:  {accuracy_test:.4f}")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'.")
