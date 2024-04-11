s = input("Nhập chuỗi: ")

chu_thuong = chu_hoa = chu_so = ky_tu_dac_biet = 0

for char in s:
    if char.islower():
        chu_thuong += 1
    elif char.isupper():
        chu_hoa += 1
    elif char.isdigit():
        chu_so += 1
    else:
        ky_tu_dac_biet += 1

print("Số lượng chữ thường:", chu_thuong)
print("Số lượng chữ hoa:", chu_hoa)
print("Số lượng chữ số:", chu_so)
print("Số lượng ký tự đặc biệt:", ky_tu_dac_biet)
