import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential

# --- 1. CHUẨN BỊ DỮ LIỆU (Bắt buộc) ---
# Tải bộ dữ liệu MNIST
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Chuẩn hóa dữ liệu: đưa pixel về khoảng [0, 1]
X_train, X_test = X_train / 255.0, X_test / 255.0

print(f"Đã tải và chuẩn bị {len(X_train)} mẫu huấn luyện.")


# --- 2. BÀI GIẢI THỰC HÀNH 1: Huấn luyện với 1 Epoch ---
print("\n--- Bài 1: Huấn luyện với epochs=1 ---")

# Định nghĩa lại mô hình gốc
model_1_epoch = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile
model_1_epoch.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Huấn luyện chỉ với 1 epoch
history_1_epoch = model_1_epoch.fit(X_train, y_train, epochs=1)

# Đánh giá trên tập Test
print("\nĐánh giá model 1 epoch trên tập Test:")
test_loss_1, test_acc_1 = model_1_epoch.evaluate(X_test, y_test, verbose=0)
print(f"Độ chính xác trên tập Test (1 epoch): {test_acc_1:.4f}")

"""
Phân tích (Bài 1):
Kết quả accuracy (thường khoảng 0.94-0.95) thấp hơn đáng kể so với 
kết quả 10 epochs (thường khoảng 0.97-0.98). 
Điều này là do mô hình bị "Underfitting" (học chưa tới). 
Nó mới chỉ nhìn qua dữ liệu 1 lần, chưa đủ thời gian để 
Gradient Descent tối ưu hóa các trọng số.
"""


# --- 3. BÀI GIẢI THỰC HÀNH 2: Thêm một Lớp ẩn ---
print("\n--- Bài 2: Thêm 1 lớp ẩn (Dense(64)) và huấn luyện 10 epochs ---")

# Định nghĩa kiến trúc mạng mới, sâu hơn
model_deeper = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),  # <--- LỚP MỚI ĐƯỢC THÊM VÀO
    Dense(10, activation='softmax')
])

# Compile
model_deeper.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Huấn luyện với 10 epochs
history_deeper = model_deeper.fit(X_train, y_train, epochs=10, verbose=0) # verbose=0 để bớt log

# Đánh giá trên tập Test
print("\nĐánh giá model sâu hơn trên tập Test:")
test_loss_deep, test_acc_deep = model_deeper.evaluate(X_test, y_test, verbose=0)
print(f"Độ chính xác trên tập Test (mạng sâu hơn): {test_acc_deep:.4f}")

"""
Phân tích (Bài 2):
Kết quả accuracy (thường ~0.97-0.98) là rất cao, 
tương đương hoặc đôi khi còn tốt hơn một chút so với mô hình gốc. 
Việc thêm lớp mới giúp tăng "năng lực" (capacity) của mô hình, 
cho phép nó học các quy luật phức tạp hơn. 
(Lưu ý: Với bài toán MNIST vốn đã đơn giản, việc thêm lớp không phải lúc nào 
cũng cải thiện nhiều, nhưng với các bài toán phức tạp hơn, 
thêm lớp là một chiến lược quan trọng).
"""
