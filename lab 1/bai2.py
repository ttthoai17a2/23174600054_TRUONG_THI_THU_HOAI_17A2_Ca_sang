class Sach:
    def __init__(ten, ma_sach, ten_sach, tac_gia, nam_xuat_ban, so_luong):
        ten.ma_sach = ma_sach
        ten.ten_sach = ten_sach
        ten.tac_gia = tac_gia
        ten.nam_xuat_ban = nam_xuat_ban
        ten.so_luong = so_luong
def main():
    # Nhập thông tin sinh viên
    so_luong_sach=int(input("Nhập số lượng sách: "))
    ma_sinh_vien=int(input("Nhâp mã sinh viên: "))
    # Tạo danh sách
    danh_sach=[]
    for i in range(so_luong_sach):
        ten_sach = input("Nhập tên sách: ")
        tac_gia = input("Nhập tác giả: ")
        nam_xuat_ban = input("Nhập năm xuất bản: ")

        sach = Sach(ma_sinh_vien, ten_sach, tac_gia, nam_xuat_ban, so_luong_sach)
        danh_sach.append(sach)
    # In thông tin
        
        # In thông tin sách
    print(f"Thư viện ĐHKTKTCN có {so_luong_sach} sách:")
    for sach in danh_sach:
        print(f"- {sach.ten_sach} với mã số {sach.ma_sach}.")
        print(f"Cuốn sách của tác giả {sach.tac_gia} được xuất bản vào năm {sach.nam_xuat_ban}")

if __name__ == "__main__":
    main()

    
