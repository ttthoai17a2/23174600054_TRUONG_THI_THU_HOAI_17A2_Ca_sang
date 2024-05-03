N = int(input("Nhập vào một số nguyên N: "))
tudien = {}

for x in range(1, N + 1):
    tudien[x] = x ** 3

print("Từ điển dạng (x, x^3):")
for key, value in tudien.items():
    print(f"{key}: {value}")
