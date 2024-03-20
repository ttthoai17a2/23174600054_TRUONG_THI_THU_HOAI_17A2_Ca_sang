#Viết chương trình nhập vào các hệ số a, b và in ra nghiệm của phương trình bậc
#nhất: ax + b = 0 (giải và biện luận đầy đủ các trường hợp).
a,b=map(int,input("Nhập vào các hệ số:").split())
if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
else:
    x = -b / a
    print("Nghiệm của phương trình là:", x)
    
