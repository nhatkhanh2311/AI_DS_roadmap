import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# --- Chuẩn bị dữ liệu (tương tự bài trên) ---
try:
    df = pd.read_csv('titanic.csv')
    df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
    df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df.dropna(inplace=True)
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- Vòng lặp tìm max_depth tốt nhất ---
    depths = range(1, 16)
    test_accuracies = []

    for depth in depths:
        tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
        tree.fit(X_train, y_train)
        y_pred = tree.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        test_accuracies.append(accuracy)

    # Tìm ra độ sâu tốt nhất
    best_accuracy = max(test_accuracies)
    best_depth = depths[test_accuracies.index(best_accuracy)]

    print("\n--- Bài 2: Tìm max_depth tối ưu ---")
    print(f"Giá trị max_depth tốt nhất là: {best_depth}")
    print(f"Với accuracy trên tập test là: {best_accuracy:.4f}")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'.")
