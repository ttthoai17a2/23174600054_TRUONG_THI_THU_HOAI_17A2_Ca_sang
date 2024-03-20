#Viết chương trình Python nhận vào một số nguyên từ người dùng và xuất ra
#chữ số hàng nghìn của số đó, nếu không có thì xuất ra 0.
n = int(input("Nhập vào số nguyên:"))
chu_so_hang_nghin = n//1000
if chu_so_hang_nghin == 0:
    print("Số không có chữ số hànng nghìn")
elif 0 < chu_so_hang_nghin <=9:
    print("Chữ số hàn g nghìn là:",chu_so_hang_nghin)
else:
    phan_du= chu_so_hang_nghin%10
    if phan_du == 0:
        print("chữ số hàng nghìn là:",0)
    else:
        print("chữ số hàng nghìn là:",phan_du)
