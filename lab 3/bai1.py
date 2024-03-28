# a
'''
n = int(input("Nhập vào một số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập lại số nguyên dương.")
else:
    sum=0
for i in range(1, n+1):
    sum = sum + i
    ket_qua=sum
print(f"Tổng S({n}) = {ket_qua}")
'''
#b
'''
n = int(input("Nhập vào một số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập lại số nguyên dương.")
else:
    tong = 0
    for i in range(1, n + 1):
        tong += 1 / i
        ket_qua=tong
print(f"Tổng S = {ket_qua}")
'''
#c
'''
import math
n = int(input("Nhập vào một số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập lại số nguyên dương.")
else:
    tong = 0
    for i in range(1, n + 1):
        tong += 1 / math.sqrt(2 * i)
        ket_qua=tong
print(f"Tổng S = {ket_qua}") 
'''
# d
n = int(input("Nhập vào một số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập lại số nguyên dương.")
else:
    tong = 0
    for i in range(1, n + 1):
        tong += (-1) ** (i + 1) / i
        ket_qua=tong
print(f"Tổng S = {ket_qua}")



