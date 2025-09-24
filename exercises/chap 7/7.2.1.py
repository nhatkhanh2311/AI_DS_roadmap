import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GRU, Dense # Import GRU thay vì LSTM

# --- 1. Tải và Chuẩn bị Dữ liệu (Tương tự bài học) ---
vocab_size = 10000
maxlen = 200
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocab_size)
X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

# --- 2. Xây dựng mô hình với GRU ---
model_gru = Sequential([
    Embedding(input_dim=vocab_size, output_dim=128, input_length=maxlen),
    GRU(64), # <-- THAY THẾ LSTM BẰNG GRU
    Dense(1, activation='sigmoid')
])

model_gru.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("--- Mô hình GRU ---")
model_gru.summary()

# --- 3. Huấn luyện mô hình ---
print("\nBắt đầu huấn luyện GRU...")
history_gru = model_gru.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.2, verbose=1)

# --- 4. Đánh giá ---
test_loss_gru, test_acc_gru = model_gru.evaluate(X_test, y_test)
print(f"\nĐộ chính xác của GRU trên tập Test: {test_acc_gru:.4f}")
