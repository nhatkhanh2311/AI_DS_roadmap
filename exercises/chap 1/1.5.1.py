# Cho một dictionary ban đầu
product_prices = {
    'apple': 15000,
    'banana': 8000,
    'orange': 25000,
    'grape': 40000
}

# Sử dụng Dictionary Comprehension để tạo dictionary mới
# Cú pháp: {new_key:new_value for (key, value) in dict.items() if condition}
# 1. Lặp qua từng cặp (product, price) trong product_prices.items()
# 2. Kiểm tra điều kiện if price > 20000
# 3. Nếu đúng, thêm cặp (product: price) vào dictionary mới
expensive_products = {
    product: price
    for (product, price) in product_prices.items()
    if price > 20000
}

print(f"Các sản phẩm có giá trên 20000: {expensive_products}")
