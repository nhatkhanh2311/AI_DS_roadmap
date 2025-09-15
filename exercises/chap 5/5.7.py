import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
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

    # --- 2. Huấn luyện và Đánh giá DecisionTreeRegressor ---
    tree_reg = DecisionTreeRegressor(random_state=42)
    tree_reg.fit(X_train, y_train)
    y_pred_tree = tree_reg.predict(X_test)
    rmse_tree = np.sqrt(mean_squared_error(y_test, y_pred_tree))
    print(f"\nRMSE của Decision Tree Regressor: {rmse_tree:.4f}")

    # --- 3. Huấn luyện và Đánh giá RandomForestRegressor ---
    forest_reg = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    forest_reg.fit(X_train, y_train)
    y_pred_forest = forest_reg.predict(X_test)
    rmse_forest = np.sqrt(mean_squared_error(y_test, y_pred_forest))
    print(f"RMSE của Random Forest Regressor: {rmse_forest:.4f}")

    """
    Nhận xét:
    Kết quả cho thấy RMSE của Random Forest (~2.96) thấp hơn đáng kể so với 
    Decision Tree đơn lẻ (~3.68). Điều này chứng tỏ việc kết hợp nhiều cây 
    đã giúp mô hình đưa ra dự đoán tổng quát và chính xác hơn, giảm thiểu 
    ảnh hưởng của overfitting từ một cây duy nhất.
    """

except Exception as e:
    print(f"Đã có lỗi xảy ra: {e}")

# --- 4. Tầm quan trọng của các đặc trưng ---
# Lấy ra tầm quan trọng của các đặc trưng từ mô hình Random Forest đã huấn luyện
importances = forest_reg.feature_importances_

# Tạo một Pandas Series để hiển thị kết quả cho dễ đọc
feature_importance_series = pd.Series(importances, index=X_train.columns)

# Sắp xếp để xem các đặc trưng quan trọng nhất
sorted_importances = feature_importance_series.sort_values(ascending=False)

print("\n--- Tầm quan trọng của các Đặc trưng (theo Random Forest) ---")
print(sorted_importances)
