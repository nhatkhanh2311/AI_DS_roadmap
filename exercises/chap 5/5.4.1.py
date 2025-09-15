import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# --- Chuẩn bị dữ liệu (tương tự bài học) ---
try:
    df = pd.read_csv('titanic.csv')
    df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
    df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df.dropna(inplace=True)
    X = df.drop('Survived', axis=1)
    y = df['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # --- Tìm k tối ưu ---
    k_values = range(1, 21)
    accuracies = []

    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train_scaled, y_train)
        y_pred = knn.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies.append(accuracy)

    # Tìm k tốt nhất
    best_k = k_values[accuracies.index(max(accuracies))]
    best_accuracy = max(accuracies)

    print("--- Bài 1: Tìm k tối ưu ---")
    print(f"Giá trị k tốt nhất là: {best_k}")
    print(f"Với accuracy trên tập test là: {best_accuracy:.4f}")

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'.")
