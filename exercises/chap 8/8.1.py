import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, UpSampling2D, Dropout
from tensorflow.keras.applications import ResNet50

# --- 1. Tải và Tiền xử lý Dữ liệu ---
# Tải bộ dữ liệu CIFAR-10
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Sử dụng hàm tiền xử lý riêng của ResNet50.
# Hàm này sẽ chuẩn hóa pixel về dải màu mà ResNet50 đã được huấn luyện.
x_train = tf.keras.applications.resnet50.preprocess_input(x_train)
x_test = tf.keras.applications.resnet50.preprocess_input(x_test)

print("Tải và xử lý dữ liệu hoàn tất.")
print("Kích thước x_train:", x_train.shape)

# --- 2. Xây dựng Mô hình ---
# Tải mô hình ResNet50 đã được huấn luyện trước trên ImageNet
# Bỏ đi lớp phân loại cuối cùng (include_top=False)
base_model_resnet = ResNet50(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# Đóng băng các trọng số của mô hình gốc để không huấn luyện lại chúng
base_model_resnet.trainable = False

# Xây dựng mô hình Sequential hoàn chỉnh
model_resnet_tl = Sequential([
    # Lớp Input cho ảnh CIFAR-10 gốc (32x32)
    tf.keras.layers.Input(shape=(32, 32, 3)),

    # Phóng to ảnh lên 224x224 để phù hợp với đầu vào của ResNet50
    UpSampling2D(size=(7, 7)),

    # Mô hình ResNet50 đã đóng băng
    base_model_resnet,

    # Các lớp phân loại mới của chúng ta
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),  # Thêm Dropout để giảm overfitting
    Dense(10, activation='softmax')  # 10 lớp cho CIFAR-10
])

print("\n--- Cấu trúc Mô hình Hoàn chỉnh ---")
model_resnet_tl.summary()

# --- 3. Compile và Huấn luyện Mô hình ---
model_resnet_tl.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("\nBắt đầu huấn luyện...")
history = model_resnet_tl.fit(
    x_train, y_train,
    epochs=5,
    batch_size=64,  # Tăng batch size để huấn luyện nhanh hơn trên GPU
    validation_data=(x_test, y_test)
)

# --- 4. Đánh giá Kết quả ---
test_loss, test_accuracy = model_resnet_tl.evaluate(x_test, y_test, verbose=0)
print(f"\nĐộ chính xác cuối cùng trên tập test: {test_accuracy:.4f}")
