n = int(input("Nhập vào một số nguyên: "))
count = 0

if n == 0:
    count = 1

while n != 0:
    count += 1
    n//= 10

print("Số chữ số của số nguyên là:", count)
