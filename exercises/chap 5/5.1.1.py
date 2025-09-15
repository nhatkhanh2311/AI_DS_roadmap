import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# --- Chuẩn bị dữ liệu (Tương tự bài học) ---
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
X = pd.DataFrame(data)
y = pd.Series(target)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 1. Tạo Đặc trưng Đa thức ---
# Khởi tạo đối tượng PolynomialFeatures với bậc 2
poly = PolynomialFeatures(degree=2, include_bias=False)

# fit_transform trên tập train
X_train_poly = poly.fit_transform(X_train)

# chỉ transform trên tập test
X_test_poly = poly.transform(X_test)

# --- 2. Huấn luyện và Đánh giá mô hình mới ---
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
y_pred_poly = poly_model.predict(X_test_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print("--- Bài 1: Kết quả Hồi quy Đa thức ---")
print(f"R-squared (R2) của mô hình đa thức: {r2_poly:.4f}")

"""
Nhận xét:
R-squared của mô hình đa thức (thường khoảng 0.79-0.81) cao hơn đáng kể 
so với mô hình tuyến tính đơn giản (khoảng 0.67). 
Điều này cho thấy việc tạo ra các đặc trưng tương tác và bậc hai 
đã giúp mô hình nắm bắt được các mối quan hệ phi tuyến trong dữ liệu, 
từ đó cải thiện hiệu năng.
"""
