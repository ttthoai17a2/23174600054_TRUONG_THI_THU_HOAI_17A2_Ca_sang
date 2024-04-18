# Tạo danh sách số nguyên tố bằng list comprehension
so_nguyen_to = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
print("Danh sách các số nguyên tố nhỏ hơn 100 là:")
print(so_nguyen_to)
