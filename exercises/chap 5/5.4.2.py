import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

# --- Chuẩn bị dữ liệu Boston Housing ---
try:
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]
    X = pd.DataFrame(data)
    y = pd.Series(target)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 1. Chuẩn hóa dữ liệu
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 2. Huấn luyện KNeighborsRegressor
    knn_reg = KNeighborsRegressor(n_neighbors=5)
    knn_reg.fit(X_train_scaled, y_train)

    # 3. Đưa ra dự đoán
    y_pred_reg = knn_reg.predict(X_test_scaled)

    # 4. Đánh giá mô hình
    rmse = np.sqrt(mean_squared_error(y_test, y_pred_reg))
    r2 = r2_score(y_test, y_pred_reg)

    print("\n--- Bài 2: KNN cho Hồi quy ---")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"R-squared (R2): {r2:.4f}")

    """
    So sánh với Linear Regression (kết quả tham khảo: RMSE ~4.92, R2 ~0.67):
    KNN Regressor (RMSE ~4.13, R2 ~0.77) hoạt động tốt hơn Linear Regression trên bộ dữ liệu này.
    """

except Exception as e:
    print(f"Đã có lỗi xảy ra. Lỗi: {e}")
