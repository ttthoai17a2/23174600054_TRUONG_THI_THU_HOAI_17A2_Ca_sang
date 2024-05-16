def cubesum(n):
    return sum(int(chu_so) ** 3 for chu_so in str(n))
def PrintArmstrong():
    for so in range(1, 1000):  
        if so == cubesum(so):
            print(so)

PrintArmstrong()
