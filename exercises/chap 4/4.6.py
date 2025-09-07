import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# --- 1. Chuẩn bị dữ liệu (Tương tự bài học) ---
try:
    # Tải bộ dữ liệu Boston housing
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]
    # Chuyển thành DataFrame
    X = pd.DataFrame(data)
    y = pd.Series(target)

    # Chia dữ liệu
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Dữ liệu đã sẵn sàng, bắt đầu huấn luyện RandomForestRegressor...")

    # --- 2. Huấn luyện mô hình RandomForestRegressor ---
    rf_model = RandomForestRegressor(random_state=42)
    rf_model.fit(X_train, y_train)

    # Đưa ra dự đoán
    y_pred_rf = rf_model.predict(X_test)

    # --- 3. Đánh giá và So sánh ---
    mae_rf = mean_absolute_error(y_test, y_pred_rf)
    mse_rf = mean_squared_error(y_test, y_pred_rf)
    rmse_rf = np.sqrt(mse_rf)
    r2_rf = r2_score(y_test, y_pred_rf)

    print("\n--- Kết quả Đánh giá Mô hình RandomForestRegressor ---")
    print(f"Mean Absolute Error (MAE): {mae_rf:.4f}")
    print(f"Mean Squared Error (MSE): {mse_rf:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse_rf:.4f}")
    print(f"R-squared (R2): {r2_rf:.4f}")

    """
    So sánh với LinearRegression (kết quả tham khảo từ bài học: RMSE ~4.92, R2 ~0.67):
    - RandomForestRegressor cho kết quả RMSE thấp hơn đáng kể (khoảng 2.9) và R2 cao hơn nhiều (khoảng 0.87).
    - MAE, MSE, và RMSE đều là các chỉ số lỗi, do đó giá trị càng thấp thì mô hình càng tốt.
    - R2 là chỉ số đo độ phù hợp, giá trị càng cao (càng gần 1) thì mô hình càng tốt.

    => Kết luận: RandomForestRegressor hoạt động tốt hơn rất nhiều so với LinearRegression trên bộ dữ liệu này.
    Điều này cho thấy mối quan hệ giữa các đặc trưng và giá nhà có thể là phi tuyến, 
    điều mà RandomForest (một mô hình phi tuyến) có thể nắm bắt tốt hơn.
    """

except Exception as e:
    print(f"Đã có lỗi xảy ra. Có thể do link tải dữ liệu đã thay đổi. Lỗi: {e}")
