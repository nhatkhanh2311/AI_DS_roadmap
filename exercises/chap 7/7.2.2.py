import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# --- 1. Tải và Chuẩn bị Dữ liệu ---
vocab_size = 10000
maxlen = 200
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocab_size)
X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

# --- 2. Xây dựng mô hình LSTM xếp chồng ---
model_stacked_lstm = Sequential([
    Embedding(input_dim=vocab_size, output_dim=128, input_length=maxlen),

    # Lớp LSTM đầu tiên phải trả về toàn bộ chuỗi output cho lớp sau
    # Bằng cách đặt return_sequences=True
    LSTM(64, return_sequences=True),

    # Lớp LSTM thứ hai nhận chuỗi đó làm input
    LSTM(32),  # Lớp cuối cùng trong chuỗi RNN không cần return_sequences

    Dense(1, activation='sigmoid')
])

model_stacked_lstm.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("--- Mô hình LSTM Xếp chồng ---")
model_stacked_lstm.summary()

# --- 3. Huấn luyện mô hình ---
print("\nBắt đầu huấn luyện LSTM xếp chồng...")
# Giảm epochs xuống 3 để chạy nhanh hơn cho ví dụ này
history_stacked = model_stacked_lstm.fit(X_train, y_train, epochs=3, batch_size=64, validation_split=0.2)

# --- 4. Đánh giá ---
test_loss_stacked, test_acc_stacked = model_stacked_lstm.evaluate(X_test, y_test)
print(f"\nĐộ chính xác của LSTM xếp chồng trên tập Test: {test_acc_stacked:.4f}")
