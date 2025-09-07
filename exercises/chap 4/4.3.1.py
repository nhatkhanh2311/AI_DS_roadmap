import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Tải lại dữ liệu gốc để thực hành
df_original = pd.read_csv('titanic.csv')
X = df_original.drop('Survived', axis=1)
y = df_original['Survived']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
median_fare = X_train['Fare'].median()
# Dùng cách gán lại an toàn
X_train['Fare'] = X_train['Fare'].fillna(median_fare)

# Lấy cột Fare và reshape lại thành mảng 2D vì Scaler yêu cầu
fare_column = X_train['Fare'].values.reshape(-1, 1)

# 1. Áp dụng StandardScaler
scaler_std = StandardScaler()
fare_standardized = scaler_std.fit_transform(fare_column)
print("5 giá trị đầu sau khi dùng StandardScaler (mean=0, std=1):")
print(fare_standardized[:5].flatten())

# 2. Áp dụng MinMaxScaler
scaler_minmax = MinMaxScaler()
fare_normalized = scaler_minmax.fit_transform(fare_column)
print("\n5 giá trị đầu sau khi dùng MinMaxScaler (range [0, 1]):")
print(fare_normalized[:5].flatten())
