def cubesum(n):
    n_str = str(n)
    
    total = sum(int(digit) ** 3 for digit in n_str)
    
    return total

n = int(input("Nhập vào một số:"))
result = cubesum(n)
print(f"Tổng các lập phương của các chữ số của {n} là {result}")  
