import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2


def df(x):
    return 2 * x


def run_gradient_descent(learning_rate, start_x=4, iterations=20):
    """Hàm để chạy và vẽ đồ thị Gradient Descent với learning rate khác nhau."""
    history = [start_x]
    current_x = start_x

    for _ in range(iterations):
        gradient = df(current_x)
        current_x = current_x - learning_rate * gradient
        history.append(current_x)

    # Vẽ đồ thị
    x_vals = np.linspace(-5, 5, 100)
    plt.plot(x_vals, f(x_vals))
    plt.plot(history, f(np.array(history)), 'o-', label=f'LR = {learning_rate}')
    plt.title(f'Gradient Descent với Learning Rate = {learning_rate}')
    plt.legend()
    plt.grid(True)
    plt.show()


# --- Chạy các thí nghiệm ---

# 1. Learning Rate rất nhỏ (0.01)
run_gradient_descent(0.01)
print("Nhận xét LR=0.01: Hội tụ rất chậm, các bước đi quá nhỏ.")

# 2. Learning Rate rất lớn (0.95)
run_gradient_descent(0.95)
print("Nhận xét LR=0.95: Hội tụ nhanh nhưng 'nhảy' qua lại giữa hai bên của điểm cực tiểu.")

# 3. Learning Rate "hoàn hảo" (0.5)
run_gradient_descent(0.5)
print("Nhận xét LR=0.5: Hội tụ trực tiếp về điểm cực tiểu chỉ trong một bước (trường hợp đặc biệt của hàm này).")

# 4. Learning Rate "thảm họa" (1.01)
run_gradient_descent(1.01, iterations=10)  # Giảm số lần lặp để thấy rõ
print("Nhận xét LR=1.01: Phân kỳ! Các bước nhảy ngày càng xa điểm cực tiểu, giá trị hàm mất mát tăng vọt.")
