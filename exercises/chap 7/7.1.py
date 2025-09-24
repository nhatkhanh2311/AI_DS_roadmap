from tensorflow.keras.preprocessing.text import Tokenizer

# 1. Dữ liệu mẫu
sentences = [
    'Tôi thích học AI',
    'AI là một lĩnh vực thú vị',
    'Tôi cũng thích Python'
]

# 2. Khởi tạo và Huấn luyện Tokenizer
# num_words=100: chỉ xem xét 100 từ phổ biến nhất
tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(sentences)

# 3. Phân tích kết quả

# a. word_index: là một dictionary ánh xạ từ mỗi từ duy nhất sang một số nguyên (ID)
# Tokenizer mặc định chuyển các từ về chữ thường.
word_index = tokenizer.word_index
print("--- Từ điển (Word Index) ---")
print(word_index)

# b. texts_to_sequences: Chuyển đổi mỗi câu thành một chuỗi các ID tương ứng
sequences = tokenizer.texts_to_sequences(sentences)
print("\n--- Chuỗi số nguyên (Sequences) ---")
print(sequences)
