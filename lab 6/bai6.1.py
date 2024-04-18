m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

print("Nhập các phần tử của ma trận:")
ma_tran = []
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(float(input("Nhập phần tử ở hàng {} cột {}: ".format(i + 1, j + 1))))
    ma_tran.append(hang)

# Tính tổng của ma trận
tong = 0
for hang in ma_tran:
    tong += sum(hang)
print("Tổng của các phần tử trong ma trận là:", tong)

# Nhập ma trận thứ h
print("\nNhập ma trận thứ hai có kích thước {}x{}".format(n, m))
print("Nhập các phần tử của ma trận:")
ma_tran_2 = []
for i in range(n):
    hang = []
    for j in range(m):
        hang.append(float(input("Nhập phần tử ở hàng {} cột {}: ".format(i + 1, j + 1))))
    ma_tran_2.append(hang)

# Tính tích của hai ma trận
if len(ma_tran[0]) == len(ma_tran_2):
    tich = []
    for i in range(len(ma_tran)):
        hang_tich = []
        for j in range(len(ma_tran_2[0])):
            tich_ij = sum(ma_tran[i][k] * ma_tran_2[k][j] for k in range(len(ma_tran[0])))
            hang_tich.append(tich_ij)
        tich.append(hang_tich)
    print("\nTích của hai ma trận là:")
    for hang in tich:
        print(hang)
else:
    print("\nKhông thể tính tích của hai ma trận vì số cột của ma trận thứ nhất không bằng số hàng của ma trận thứ hai.")

print("\nMa trận chuyển vị của ma trận ban đầu là:")
chuyen_vi = [[ma_tran[j][i] for j in range(len(ma_tran))] for i in range(len(ma_tran[0]))]
for hang in chuyen_vi:
    print(hang)
    
