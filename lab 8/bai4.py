def sumPdivisors(n):
    if n <= 1:
        return 0
    
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    
    return total

n = int(input("Nhập vào một số:"))
print(f"Tổng các ước số chính của {n} là {sumPdivisors(n)}")  
