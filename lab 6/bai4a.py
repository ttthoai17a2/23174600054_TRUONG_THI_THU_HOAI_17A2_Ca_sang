n = int(input("Nhập số lượng số Fibonacci muốn tạo: "))

# Tạo danh sách Fibonacci bằng list comprehension
danh_sach_fibonacci = [0, 1] if n > 1 else [0] if n == 1 else []
[danh_sach_fibonacci.append(danh_sach_fibonacci[-1] + danh_sach_fibonacci[-2]) for _ in range(2, n)]
print("Danh sách Fibonacci gồm", n, "số đầu tiên là:")
print(danh_sach_fibonacci)
