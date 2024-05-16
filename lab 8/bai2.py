import math

def hoan_vi(n, r):
    if r > n:
        return 0
    return math.factorial(n) // math.factorial(n - r)

def to_hop(n, r):
    if r > n:
        return 0
    return hoan_vi(n, r) // math.factorial(r)

print("Hoán vị P(5, 3):", hoan_vi(5, 3))  
print("Tổ hợp C(5, 3):", to_hop(5, 3))   

print("Hoán vị P(6, 2):", hoan_vi(6, 2)) 
print("Tổ hợp C(6, 2):", to_hop(6, 2))    
