import requests


def get_hanoi_weather():
    """
    Lấy thông tin thời tiết hiện tại của Hà Nội từ API wttr.in.
    """
    # 1. URL của API endpoint cho Hà Nội, định dạng JSON
    url = "https://wttr.in/Hanoi?format=j1"

    print("--- Lấy dữ liệu thời tiết Hà Nội ---")

    try:
        # 2. Gửi yêu cầu GET
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP (4xx hoặc 5xx)

        # 3. Chuyển đổi kết quả sang dạng dictionary
        data = response.json()

        # 4. Trích xuất thông tin cần thiết
        # Dữ liệu thời tiết hiện tại nằm trong list 'current_condition'
        current_weather = data['current_condition'][0]
        temp_c = current_weather['temp_C']
        weather_description = current_weather['weatherDesc'][0]['value']

        print(f"Nhiệt độ hiện tại: {temp_c}°C")
        print(f"Tình hình thời tiết: {weather_description}")

    except requests.exceptions.RequestException as e:
        print(f"Đã xảy ra lỗi khi gọi API: {e}")


# Chạy hàm
get_hanoi_weather()
