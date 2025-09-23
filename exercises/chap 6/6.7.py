import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import matplotlib.pyplot as plt
import numpy as np
import requests
from PIL import Image
from io import BytesIO

# --- 1. Tải và Chuẩn bị dữ liệu CIFAR-10 ---
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0

# Định nghĩa các tên lớp của CIFAR-10
class_names = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]

# --- 2. Xây dựng và Huấn luyện Mô hình ---
# (Đây là mô hình từ bài học, chúng ta huấn luyện lại nó)
print("Đang xây dựng và huấn luyện mô hình CNN...")
model_cnn = Sequential([
    Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

model_cnn.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Chỉ huấn luyện 5 epochs để chạy nhanh hơn cho bài tập này
model_cnn.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test), verbose=1)
print("Huấn luyện hoàn tất.")


# --- 3. Định nghĩa hàm dự đoán ---
def predict_image_from_url(url, model, class_names):
    """
    Tải ảnh từ URL, tiền xử lý và dự đoán bằng mô hình đã huấn luyện.
    """
    try:
        # Tải ảnh
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        # Tiền xử lý ảnh
        img_resized = img.resize((32, 32))  # Thay đổi kích thước về 32x32
        img_array = tf.keras.preprocessing.image.img_to_array(img_resized)

        # Chuẩn hóa (chia cho 255.0)
        img_normalized = img_array / 255.0

        # Thêm một chiều (batch size)
        img_expanded = np.expand_dims(img_normalized, axis=0)

        # Dự đoán
        predictions = model.predict(img_expanded)

        predicted_index = np.argmax(predictions)
        predicted_class = class_names[predicted_index]
        confidence = np.max(predictions)

        # Hiển thị kết quả
        plt.imshow(img_resized)
        plt.title(f"Dự đoán: {predicted_class} ({confidence:.2%})")
        plt.axis('off')
        plt.show()

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


# --- 4. Chạy dự đoán ---
print("\n--- Bắt đầu Bài thực hành 1 ---")
image_url_to_test = "https://cdn.wcs.org/2024/03/13/21/14/05/2d2c6f1b-71c4-4390-b7e2-deb21a0bc11f/shutterstock_2331893385.jpg"
predict_image_from_url(image_url_to_test, model_cnn, class_names)
