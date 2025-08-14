def reverse_string(s):
    """
    Đảo ngược một chuỗi bằng phương pháp đệ quy.
    """
    # 1. Trường hợp cơ sở (Base Case):
    # Nếu chuỗi rỗng hoặc chỉ có 1 ký tự, đảo ngược của nó là chính nó.
    if len(s) <= 1:
        return s

    # 2. Bước đệ quy (Recursive Step):
    # Kết quả là: đảo ngược của phần còn lại của chuỗi + ký tự đầu tiên.
    # Ví dụ: reverse("hello") = reverse("ello") + "h"
    #          reverse("ello")  = reverse("llo") + "e"
    #          ...
    return reverse_string(s[1:]) + s[0]


# Ví dụ sử dụng
my_string = "hello"
reversed_str = reverse_string(my_string)
print(f"Chuỗi gốc: {my_string}")
print(f"Chuỗi đảo ngược: {reversed_str}")
