n = int(input("Nhập số từ bàn phím: "))
count = 1
a = n 
while True:
    a = a//10  
    if a == 0:
        break
    count += 1 

for i in range(count,0,-1):
    chu_so = n//(10**(i-1))
    if chu_so == 0:
        print(" ", end = " ")
        n = n % (10**(i-1))
    elif chu_so == 1:
        print("one", end = " ")
        n = n % (10**(i-1))
    elif chu_so == 2:
        print("two", end = " ")
        n = n % (10**(i-1))
    elif chu_so == 3:
        print("three", end = " ")
        n = n % (10**(i-1))
    elif chu_so == 4:
        print("four", end = " ")
        n = n % (10**(i-1))
    elif chu_so== 5:
        print("five", end = " ")
        n = n % (10**(i-1))
    elif chu_so == 6:
        print("six", end = " ")
        n = n % (10**(i-1))
    elif chu_so == 7:
        print("seven", end = " ")
        n = n % (10**(i-1))
    elif chu_so == 8:
        print("eight", end = " ")
        n = n % (10**(i-1))
    elif chu_so == 9:
        print("nine", end = " ")
        n = n % (10**(i-1))