chuoi_day_so = input("Nhập dãy các số nguyên, cách nhau bằng khoảng trắng: ")
day_so = list(map(int, chuoi_day_so.split()))

# Kiểm tra xem dãy số tạo thành cấp số cộng hay không
la_csc = True
if len(day_so) >= 2:
    sai_so = day_so[1] - day_so[0]  # Tính sai số giữa hai phần tử đầu tiên
    for i in range(2, len(day_so)):
        if day_so[i] - day_so[i-1] != sai_so:  # Kiểm tra sai số giữa các phần tử
            la_csc = False
            break

if la_csc:
    print("Dãy số", chuoi_day_so, "tạo thành cấp số cộng.")
else:
    print("Dãy số", chuoi_day_so, "không tạo thành cấp số cộng.")
