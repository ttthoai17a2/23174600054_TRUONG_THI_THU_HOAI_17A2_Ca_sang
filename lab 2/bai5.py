'''Viết chương trình Python để tính tổng số tiền phải trả khi mua vé xem phim
với số lượng người khác nhau, trong đó:
+ Giá vé cho 1 người là 120.000 đồng.
+ Nếu số người là 2 đến 4, giảm 5% tổng số tiền.
+ Nếu số người là 4 đến 10, giảm 10% tổng số tiền.
+ Nếu số người là từ 10 người trở lên, giảm 20% tổng số tiền.
Số lượng người sẽ được nhập từ bàn phím'''
gia_ve = 120000
so_nguoi = int(input("Nhập số lượng người: "))
tong_tien = so_nguoi * gia_ve
if 2 <= so_nguoi <= 4:
    tong_tien *= 0.95  
elif 4 < so_nguoi <= 10:
    tong_tien *= 0.9  
elif so_nguoi > 10:
    tong_tien *= 0.8  
print("Tổng số tiền phải trả là:", tong_tien, "VNĐ")
