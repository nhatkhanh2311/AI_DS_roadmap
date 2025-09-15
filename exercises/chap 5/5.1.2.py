import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# --- Chuẩn bị dữ liệu đa thức (Tương tự bài 1) ---
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
X = pd.DataFrame(data)
y = pd.Series(target)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

print("\n--- Bài 2: Kết quả Ridge và Lasso ---")
# --- 1. Thử nghiệm Ridge (L2 Regularization) ---
print("\n--- Ridge Regression ---")
for alpha in [0.1, 1.0, 10.0]:
    ridge_model = Ridge(alpha=alpha)
    ridge_model.fit(X_train_poly, y_train)
    y_pred_ridge = ridge_model.predict(X_test_poly)
    r2_ridge = r2_score(y_test, y_pred_ridge)
    print(f"Với alpha = {alpha}, R2 = {r2_ridge:.4f}")

# --- 2. Thử nghiệm Lasso (L1 Regularization) ---
print("\n--- Lasso Regression ---")
for alpha in [0.01, 0.1, 1.0]:  # Lasso nhạy cảm hơn nên dùng alpha nhỏ hơn
    # tăng max_iter để đảm bảo thuật toán hội tụ
    lasso_model = Lasso(alpha=alpha, max_iter=10000)
    lasso_model.fit(X_train_poly, y_train)
    y_pred_lasso = lasso_model.predict(X_test_poly)
    r2_lasso = r2_score(y_test, y_pred_lasso)
    print(f"Với alpha = {alpha}, R2 = {r2_lasso:.4f}")

    # Đếm số lượng hệ số bị đưa về 0
    num_zero_coeffs = np.sum(lasso_model.coef_ == 0)
    print(f"   -> Số lượng đặc trưng bị loại bỏ (hệ số = 0): {num_zero_coeffs}")
