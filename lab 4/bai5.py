import math

while True:
    a1,a2= map(int, input("Nhập vào hai số a và b: ").split())
    
    
    print("Kết quả các phép tính:")
    print("Tổng:", a1 + a2)
    print("Hiệu:", a1 - a2)
    print("Tích:", a1 * a2)
    if a1 != 0:
        print("Thương:", a1 / a2)
    else:
        print("Không thể chia cho 0")
    print("Lũy thừa:", a1 ** a2)
    
    if a1 >= 0:
        print("Căn bậc hai của số thứ nhất:", math.sqrt(a1))
    else:
        print("Không thể tính căn bậc hai của số âm")

    if a2 >= 0:
        print("Căn bậc hai của số thứ hai:", math.sqrt(a2))
    else:
        print("Không thể tính căn bậc hai của số âm")
        
    
    tiep_tuc = input("Bạn có muốn tiếp tục không? (có/không): ")
    if tiep_tuc.lower() != 'có':
        break

