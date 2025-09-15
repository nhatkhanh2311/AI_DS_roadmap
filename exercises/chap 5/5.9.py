import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix

# --- 1. CHUẨN BỊ DỮ LIỆU ---
try:
    df = pd.read_csv('titanic.csv')
    df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

    median_age = df['Age'].median()
    df['Age'] = df['Age'].fillna(median_age)

    mode_embarked = df['Embarked'].mode()[0]
    df['Embarked'] = df['Embarked'].fillna(mode_embarked)

    df.dropna(inplace=True)

    X = df.drop('Survived', axis=1)
    y = df['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    numeric_features = ['Age', 'Fare', 'SibSp', 'Parch']
    categorical_features = ['Pclass', 'Sex', 'Embarked']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(), categorical_features)
        ])

    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    print("Dữ liệu đã được tiền xử lý. Bắt đầu giải bài tập...")

    # --- BÀI 1: ÁP DỤNG PCA ---
    print("\n--- Bài 1: Áp dụng PCA ---")

    # Khởi tạo PCA để giảm xuống 2 thành phần
    pca = PCA(n_components=2, random_state=42)

    # Fit và transform dữ liệu huấn luyện
    X_train_pca = pca.fit_transform(X_train_processed)

    print(f"Kích thước dữ liệu gốc (sau tiền xử lý): {X_train_processed.shape}")
    print(f"Kích thước dữ liệu sau khi giảm chiều với PCA: {X_train_pca.shape}")

    # --- BÀI 2: TRỰC QUAN HÓA CÁC LỚP ---
    print("\n--- Bài 2: Trực quan hóa kết quả PCA ---")

    # Tạo một DataFrame từ kết quả PCA để vẽ bằng Seaborn cho dễ
    pca_df = pd.DataFrame(data=X_train_pca, columns=['PC1', 'PC2'])
    pca_df['label'] = y_train.values  # Gán nhãn thật (y_train) vào

    plt.figure(figsize=(10, 7))
    sns.scatterplot(x='PC1', y='PC2', hue='label', data=pca_df, alpha=0.7)
    plt.title('Dữ liệu Titanic sau khi giảm chiều bằng PCA (tô màu theo nhãn thật)')
    plt.legend(title='Sống sót (1) / Tử vong (0)')
    plt.grid(True)
    plt.show()

    """
    PHÂN TÍCH BIỂU ĐỒ (BÀI 2):
    - Câu trả lời là CÓ, chúng ta CÓ THỂ THẤY SỰ TÁCH BIỆT (ở một mức độ nhất định).
    - Biểu đồ cho thấy hai lớp (0 - Tử vong và 1 - Sống sót) không bị trộn lẫn hoàn toàn ngẫu nhiên. 
    - Có những khu vực rõ rệt mà các điểm màu cam (Sống sót) tập trung nhiều hơn và ngược lại.
    - Tuy nhiên, hai cụm này đè lên nhau đáng kể ở khu vực trung tâm, cho thấy bài toán này
      rất phức tạp và không thể phân tách một cách hoàn hảo chỉ bằng 2 đặc trưng tuyến tính.
    - Điều này cho chúng ta biết: Các đặc trưng gốc (trước khi PCA) CÓ chứa thông tin hữu ích để 
      phân loại, và một mô hình học máy (có giám sát) có khả năng sẽ học được đường ranh giới
      để phân tách chúng.
    """

    # --- BÀI 3: ÁP DỤNG K-MEANS ---
    print("\n--- Bài 3: Áp dụng K-Means trên dữ liệu PCA ---")

    # Huấn luyện K-Means để tìm 2 cụm (vì ta biết có 2 lớp)
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    kmeans_labels = kmeans.fit_predict(X_train_pca)

    # So sánh kết quả của K-Means (không giám sát) với nhãn thật (có giám sát)
    # Lưu ý: Nhãn 0 của K-Means có thể tương ứng với nhãn 1 của nhãn thật và ngược lại.
    print("Ma trận nhầm lẫn giữa Nhãn thật (y_train) và Nhãn của K-Means:")
    cm = confusion_matrix(y_train, kmeans_labels)
    print(cm)

    """
    PHÂN TÍCH (BÀI 3):
    - Ma trận nhầm lẫn (confusion matrix) sẽ cho bạn thấy K-Means đã phân nhóm dữ liệu.
    - Tuy nhiên, K-Means (một thuật toán không giám sát) chỉ cố gắng tìm các cụm 
      dựa trên khoảng cách, nó không biết gì về nhãn "Sống sót". 
    - Kết quả của nó sẽ không chính xác bằng một thuật toán CÓ GIÁM SÁT 
      (như Logistic Regression) được huấn luyện để TỐI ƯU HÓA việc phân loại đúng.
    - Bài tập này cho thấy sự khác biệt giữa "phân cụm" và "phân loại".
    """

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'.")
except Exception as e:
    print(f"Đã có lỗi xảy ra: {e}")
