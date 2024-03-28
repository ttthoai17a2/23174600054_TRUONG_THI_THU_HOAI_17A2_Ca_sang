# a
'''
print("Các số nt từ 100 đến 1000 là:")
for i in range(100, 1001):
        for j in range(2, int(i**0.5)+1):
            if i%j==0:  
                break
        else:  
            print(i,end=' ')


#b
print("Các  số chình phương là:")
for i in range(1,32):
    print(i**2)


#c
a, b = 0, 1
print(a)
for i in range(1,101):  
    if b >= 100:
        break
    print(b)
    a, b = b, a + b

#d
for i in range(1, 501):
    sum=0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)
'''
#e
total = 0
for n in range(1, 201):
    total += n * (3 * n - 1) // 2

print(total)
