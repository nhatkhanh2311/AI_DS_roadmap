python_students = ["An", "Bảo", "Chi", "Dũng", "Giang"]
web_students = ["Chi", "Dũng", "Hùng", "Lan", "An"]

# Chuyển hai list thành hai set để thực hiện các phép toán tập hợp
python_set = set(python_students)
web_set = set(web_students)

# a. Tìm sinh viên học cả hai khóa (phép giao - intersection)
both_courses = python_set.intersection(web_set)
print(f"Sinh viên học cả hai khóa: {both_courses}")
print(f"Tổng số sinh viên học cả hai khóa: {len(both_courses)}")

# b. Tìm tổng số sinh viên (phép hợp - union)
all_students = python_set.union(web_set)
print(f"\nDanh sách tất cả sinh viên: {all_students}")
print(f"Tổng số sinh viên: {len(all_students)}")


# c. Tìm sinh viên chỉ học Python (phép hiệu - difference)
python_only = python_set.difference(web_set)
print(f"\nSinh viên chỉ học Python: {python_only}")
