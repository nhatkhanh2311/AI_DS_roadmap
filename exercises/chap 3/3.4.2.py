import requests
from bs4 import BeautifulSoup


def scrape_vnexpress_titles():
    """
    Lấy 5 tiêu đề tin tức đầu tiên từ trang chủ VnExpress.
    """
    # 1. URL trang chủ
    url = "https://vnexpress.net/"

    print("\n--- Lấy tiêu đề từ VnExpress ---")

    try:
        # 2. Dùng requests để lấy mã HTML
        # Thêm header 'User-Agent' để giả lập một trình duyệt thông thường
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # 3. Dùng BeautifulSoup để parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 4. Tìm các thẻ chứa tiêu đề
        # Dựa trên việc "Inspect" trang web, các tiêu đề chính thường nằm trong
        # thẻ <h3> có class là 'title-news' hoặc các biến thể tương tự.
        # Chúng ta sẽ tìm tất cả các thẻ h3 có class chứa "title-news".
        titles = soup.select("h3.title-news a")

        # 5. In ra 5 tiêu đề đầu tiên
        print("5 tiêu đề hàng đầu:")
        count = 0
        for title in titles:
            if count < 5:
                # .get_text() để lấy nội dung text, .strip() để xóa khoảng trắng thừa
                print(f"- {title.get_text(strip=True)}")
                count += 1
            else:
                break

    except requests.exceptions.RequestException as e:
        print(f"Đã xảy ra lỗi khi truy cập trang web: {e}")


# Chạy hàm
scrape_vnexpress_titles()
