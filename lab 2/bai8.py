'''Hãy viết chương trình Python để xác định vị trí tương đối của hai đường thẳng
trong không gian hai chiều. Hãy nhập thông số của hai đường thẳng (hệ số góc
và hệ số tự do) và in ra kết quả vị trí tương đối của hai đường thẳng (đường
thẳng song song, đường thẳng cắt nhau hay đường thẳng vuông góc).'''

a,b=map(int,input("Nhập hệ số góc:").split())
c,d= map(int,input("Nhập hệ số tự do:").split())
if a == b:
    print("Hai đường thẳng là song song")
elif a * b == -1:
        print("Hai đường thẳng là vuông góc")
else:
        print("Hai đường thẳng cắt nhau")

