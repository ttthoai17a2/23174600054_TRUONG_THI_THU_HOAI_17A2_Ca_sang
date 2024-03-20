#Viết chương trình Python để nhập vào 3 số nguyên từ bàn phím (n là số nguyên
#dương), sau đó tìm và in ra số lớn thứ hai trong các số nguyên đó.
a,b,c=map(int,input("Nhập 3 số nguyên:").split())
if a >= b and a >= c:
    if b >= c:
        max2 = b
    else:
        max2 = c
elif b >= a and b >= c:
    if a >= c:
        max2 = a
    else:
        max2 = c
else:
    if a >= b:
        max2= a
    else:
        max2= b

# In ra số lớn thứ hai
print("Số lớn thứ hai là:", max2)