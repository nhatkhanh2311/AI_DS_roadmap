import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# --- 1. Chuẩn bị dữ liệu Boston Housing ---
try:
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

    # Gán tên cột cho dễ theo dõi
    feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]
    X = pd.DataFrame(data, columns=feature_names)
    y = pd.Series(target)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Dữ liệu đã sẵn sàng, bắt đầu huấn luyện...")

    # --- 2. Huấn luyện và Đánh giá GradientBoostingRegressor ---
    # Sử dụng các tham số mặc định (n_estimators=100, learning_rate=0.1, max_depth=3)
    gb_reg = GradientBoostingRegressor(random_state=42)
    gb_reg.fit(X_train, y_train)

    y_pred_gb = gb_reg.predict(X_test)

    rmse_gb = np.sqrt(mean_squared_error(y_test, y_pred_gb))

    print(f"\nRMSE của Gradient Boosting Regressor: {rmse_gb:.4f}")

    """
    So sánh với RandomForestRegressor (RMSE ~2.96):

    Kết quả của GradientBoostingRegressor (RMSE ~2.81) cho thấy nó hoạt động tốt hơn một chút 
    so với Random Forest chỉ với các tham số mặc định.

    Đây là điều thường thấy, vì Boosting là một thuật toán tập trung vào việc sửa lỗi tuần tự (giảm bias), 
    nên thường có xu hướng "nhích" thêm một chút về độ chính xác. Bằng cách tinh chỉnh
    thêm các siêu tham số, cả hai mô hình đều có thể đạt hiệu năng tốt hơn nữa.
    """

except Exception as e:
    print(f"Đã có lỗi xảy ra: {e}")
