import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Đảm bảo bạn đã có file titanic.csv
try:
    df = pd.read_csv('titanic.csv')
    print("Đã đọc file titanic.csv thành công. Bắt đầu giải bài tập...")
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'titanic.csv'. Vui lòng đảm bảo file đã được tải và đặt đúng thư mục.")
    df = None

if df is not None:
    # --- Bài 1: Phân tích Biến Fare (Giá vé) ---
    print("\n--- Bài 1: Phân tích Biến Fare (Giá vé) ---")

    # a. Vẽ biểu đồ Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='Fare', bins=50, kde=True)
    plt.title('Phân phối Giá vé (Fare) của Hành khách')
    plt.xlabel('Giá vé')
    plt.ylabel('Số lượng')
    plt.show()

    """
    b. Phân tích và Nhận xét:
    - Nhận xét về phân phối: Biểu đồ bị lệch phải (right-skewed) rất mạnh. 
      Điều này có nghĩa là đại đa số hành khách trả một mức giá vé rất thấp (cột cao nhất ở gần 0),
      trong khi có một số ít hành khách trả một mức giá vé cực kỳ cao, tạo ra một cái "đuôi" dài về phía bên phải.

    - Mean hay Median tốt hơn?: Trong trường hợp phân phối bị lệch mạnh và có nhiều giá trị ngoại lai (outliers)
      như thế này, **Median (trung vị)** là thước đo khuynh hướng trung tâm tốt hơn.
      Lý do là vì Mean (trung bình) sẽ bị các giá trị vé cực kỳ cao "kéo" về phía nó, 
      tạo ra một con số không thực sự đại diện cho một hành khách "điển hình". 
      Median, là giá trị ở giữa, không bị ảnh hưởng bởi các giá trị ngoại lai này.
    """
    print("Phân tích cho Bài 1 đã được ghi chú trong code.")

    # --- Bài 2: So sánh giữa các Giới tính ---
    print("\n--- Bài 2: So sánh Tuổi giữa các Giới tính ---")

    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='Sex', y='Age')
    plt.title('Phân phối Tuổi theo Giới tính')
    plt.xlabel('Giới tính')
    plt.ylabel('Tuổi')
    plt.show()

    """
    Nhận xét từ biểu đồ Box Plot:
    - Tuổi trung vị (đường kẻ giữa hộp) của nam (male) có vẻ cao hơn một chút so với nữ (female).
    - Khoảng tứ phân vị (chiều cao của hộp) của nam cũng có vẻ rộng hơn một chút, 
      cho thấy 50% dữ liệu ở giữa của nam có độ phân tán về tuổi lớn hơn.
    - Nhìn chung, phân phối tuổi của hai giới khá tương đồng, nhưng nam giới có xu hướng lớn tuổi hơn một chút.
    """
    print("Phân tích cho Bài 2 đã được ghi chú trong code.")

    # --- Bài 3: Khám phá Tỷ lệ Sống sót ---
    print("\n--- Bài 3: Khám phá Tỷ lệ Sống sót theo Hạng vé ---")

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Pclass', hue='Survived')
    plt.title('Số lượng Sống sót và Tử vong theo Từng Hạng vé')
    plt.xlabel('Hạng vé (Pclass)')
    plt.ylabel('Số lượng hành khách')
    # Thay đổi chú giải để dễ đọc hơn
    plt.legend(title='Tình trạng', labels=['Tử vong', 'Sống sót'])
    plt.show()

    """
    Nhận xét từ biểu đồ Count Plot:
    Biểu đồ này cho thấy một mối liên hệ cực kỳ rõ ràng giữa hạng vé và khả năng sống sót.
    - Hạng 1 (Pclass=1): Số người sống sót (cột cam) nhiều hơn đáng kể so với số người tử vong (cột xanh).
    - Hạng 2 (Pclass=2): Số người tử vong và sống sót gần như bằng nhau.
    - Hạng 3 (Pclass=3): Số người tử vong chiếm đa số áp đảo so với số người sống sót.

    => Kết luận: Hành khách đi vé hạng càng cao thì cơ hội sống sót càng lớn.
    """
    print("Phân tích cho Bài 3 đã được ghi chú trong code.")
