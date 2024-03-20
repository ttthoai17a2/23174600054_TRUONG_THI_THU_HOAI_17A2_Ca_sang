'''# bài 1
# tạo biến tên gọi là retained
retained =100
# Giả sử có thể đầu tư số tiền này với lãi suât là 15%/năm và phần lãi suất này sẽ luu trữ với các tên là Internet
Internet =0,15
# khi đó,sau 1 năm chúng ta sẽ có 100*1,15; sau 2 năm chúng ta sẽ có 100* 1,15*1,15=132,25
total=float(retained *(1+0.15)**10)
print("số tiền nhận được sau 10 năm là:{:.2f}".format(total))'''

'''# bài 3
print(
    """


""")
'''

'''# bài 4
# bước 1 nhập nhiệt độ C từ bàn phím
nhiet_do_C = float(input("Nhập nhiệt độ :"))
# bước 2 đổi đơn vị từ độ C sang độ K
nhiet_do_K = nhiet_do_C +273.15
# bước 3: in ra kết quả ra màn hình
print("{} độ C chuyển sang độ K là {}".format(nhiet_do_C, nhiet_do_K))'''


'''# Bài 5:  viết chương trình nhập vào 2 số nguyên dương m và n (m>n), hãy in ra màn hình phần nguyên và phần dư
m,n=map(int,input("Nhập số nguyên dương:").split(','))
print("Phần nguyên của phép chia là{}".format(m//n))
print("Phần dư của phép chia m và n là{}".format(m%n))'''

# Bài6
import math
'''r=float(input("Nhập bán kính:"))
h=float(input("Nhập chiều cao:"))
s=math.pi*r*r
print("Diện tích hình tròn là:",s)'''

# Bài 7
# Nhiêht độ h
'''h=float(input("Nhập độ cao:"))
# tính vận tốc rơi tự do
g=9.8 # m/s^2,gia tốc
v1=math.sqrt(2*g*h)
v2=(2*g*h)**0.5
print("Vận tốc rơi tự do 1 là{:,2f} m/s".format(v1))
print("Vận tốc rơi tự do 2 là{:,2f} m/s".format(v2))'''

'''# Bài 8:
a,b,h=map(float,input("Nhập số đo:").split())
# tính S hình thang
s=(a+b)*h/2
print("Diện tích hình thang với đáy lớn {},đáy bé{}, chiều cao{} là:".format(a,b,h),s)'''

'''# Bài 9
a,b,c= map(float,input("Nhập các số đo:").split())
# tính và in ra chu vi dien tích tam giác
d= a+b+c
p=d/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("chu vi tam giác là{}và dien tích của tan giác là:{}".format(d,s))'''


'''# bài 10
x,y=map(float,input("Nhập các số x,y:").split())
# tính và in ra kết quả
tu=math.sin(x)
mau=(2*x+y)/math.cos(x)-x**y/(x-y)
print("Kết quả là:",tu/mau)'''

'''
# Bài 2:
#
s,m,h,d= map(int,input("Nhập các giá trị:").split())
d_s=d*24*60*60
h_s=h*60*60
m_s=m*60
thoi_gian=d_s+h_s+m_s
print("chuyển sang giây:",thoi_gian)
'''
