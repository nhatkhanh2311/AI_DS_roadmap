import numpy as np


def simulate_dice_rolls(num_rolls):
    """
    Mô phỏng việc tung một con xúc xắc và đếm tần suất mỗi mặt.
    """
    # np.random.randint(low, high, size) tạo ra các số nguyên ngẫu nhiên
    # từ low (bao gồm) đến high (không bao gồm).
    # Do đó, low=1 và high=7 sẽ tạo ra các số từ 1 đến 6.
    rolls = np.random.randint(1, 7, size=num_rolls)

    # np.unique trả về các giá trị duy nhất và số lần xuất hiện của chúng
    faces, counts = np.unique(rolls, return_counts=True)

    print(f"Kết quả mô phỏng {num_rolls} lần tung xúc xắc:")
    # Dùng zip để duyệt qua cả mặt và số đếm cùng lúc
    for face, count in zip(faces, counts):
        print(f"Mặt {face}: xuất hiện {count} lần")


# Chạy mô phỏng với 1000 lần tung
simulate_dice_rolls(1000)
