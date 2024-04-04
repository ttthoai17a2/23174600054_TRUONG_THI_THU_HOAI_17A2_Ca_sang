
numbers = []
tong =0

while tong <= 1000:
    n = int(input("Nhập một số nguyên dương: "))
    if n >0:
        tong += n
        if n % 2 != 0:
            numbers.append(n)
print("Các số lẻ đã nhập",numbers)
