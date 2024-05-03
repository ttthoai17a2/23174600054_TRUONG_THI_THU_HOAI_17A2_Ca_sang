kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
hoa_don = {}
mua_hang = {
    "banana": 3,
    "orange": 2,
    "apple": 1,
    "pear": 1
}

# Tính toán hóa đơn
tong_tien = 0
for mat_hang, so_luong in mua_hang.items():
    don_gia = gia_tien[mat_hang]
    thanh_tien = don_gia * so_luong
    tong_tien += thanh_tien
    hoa_don[mat_hang] = {
        "số lượng": so_luong,
        "đơn giá": don_gia,
        "số tiền": thanh_tien
    }

print("Hóa đơn mua hàng:")
for mat_hang, thong_tin in hoa_don.items():
    print(f"Mặt hàng: {mat_hang}")
    for key, value in thong_tin.items():
        print(f"{key}: {value}")
    print()

print("Tổng số tiền của hóa đơn:", tong_tien)
print("\nSố lượng của các mặt hàng trong kho sau khi mua:")
for mat_hang, so_luong in kho.items():
    print(f"{mat_hang}: {so_luong - mua_hang.get(mat_hang, 0)}")
