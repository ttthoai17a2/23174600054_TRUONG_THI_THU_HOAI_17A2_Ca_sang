def cubesum(n):
    return sum(int(chu_so) ** 3 for chu_so in str(n))

def isArmstrong(n):
    return n == cubesum(n)

n = int(input("Nhập vào một số:"))
print(f"Số {n} có phải là số Armstrong không? {isArmstrong(n)}")  
