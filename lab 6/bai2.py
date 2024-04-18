n = int(input("Nhập số lượng phần tử trong mảng: "))
mang = []
print("Nhập các phần tử của mảng:")
for i in range(n):
    num = int(input())
    mang.append(num)

#  số nguyên tố trong mảng
print("Các số nguyên tố trong mảng là:")
for num in mang:
    if num > 1:
        la_so_nguyen_to = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                la_so_nguyen_to = False
                break
        if la_so_nguyen_to:
            print(num)

#số hoàn hảo trong mảng
print("Các số hoàn hảo trong mảng là:")
for num in mang:
    if num > 1:
        tong_uoc = sum(i for i in range(1, num) if num % i == 0)
        if tong_uoc == num:
            print(num)
