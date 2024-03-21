'''Hãy viết chương trình Python để kiểm tra vị trí tương đối giữa một đường
thẳng và một đường tròn trong không gian hai chiều. Hãy nhập các thông số
của đường thẳng (hệ số góc và hệ số tự do) và các thông số của đường tròn (tọa
độ tâm và bán kính). Sau đó, chương trình sẽ xác định vị trí tương đối giữa
đường thẳng và đường tròn (đường thẳng cắt đường tròn, đường thẳng tiếp
xúc đường tròn, đường thẳng nằm ngoài đường tròn hay đường thẳng nằm
trong đường tròn) và in ra kết quả tương ứng.'''
import math
a, b = map(float, input("Nhập hệ số góc và  tự do của đường thẳng : ").split()) 
c,d = map(float, input("Nhập tọa độ tâm(c,d): ").split())
n = float(input("Nhập bán kính: "))
pt = abs(a*c -d +b) / math.sqrt(a**2 + 1)
if pt < n:
    print("Đường thẳng cắt đường tròn.")
elif pt == n:
    print("Đường thẳng tiếp xúc đường tròn.")
elif pt > n:
    print("Đường thẳng nằm ngoài đường tròn.")
else:
    print("Đường thẳng nằm trong đường tròn.")