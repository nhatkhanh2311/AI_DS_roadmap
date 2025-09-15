import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# --- 1. Chuẩn bị dữ liệu ---
try:
    # Tải bộ dữ liệu Boston housing
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]
    X = pd.DataFrame(data)
    y = pd.Series(target)

    # Chia dữ liệu
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Dữ liệu đã sẵn sàng. Bắt đầu giải bài tập...")

    # --- 2. Tạo bài toán Phân loại ---
    # Tìm giá trị trung vị của toàn bộ target y
    median_price = y.median()
    print(f"\nGiá nhà trung vị: {median_price}")

    # Tạo ra nhãn phân loại mới
    # Nếu giá nhà > trung vị thì nhãn là 1, ngược lại là 0
    y_train_clf = (y_train > median_price).astype(int)
    y_test_clf = (y_test > median_price).astype(int)

    print("\nVí dụ 5 nhãn hồi quy và nhãn phân loại tương ứng:")
    print(y_train.head())
    print(y_train_clf.head())

    # --- 3. Chuẩn hóa dữ liệu ---
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # --- 4. Huấn luyện và Đánh giá ---
    log_model = LogisticRegression(random_state=42)
    log_model.fit(X_train_scaled, y_train_clf)

    y_pred_clf = log_model.predict(X_test_scaled)

    print("\n--- Kết quả Đánh giá Mô hình Hồi quy Logistic ---")
    print(classification_report(y_test_clf, y_pred_clf))

except Exception as e:
    print(f"Đã có lỗi xảy ra. Có thể do link tải dữ liệu đã thay đổi. Lỗi: {e}")
