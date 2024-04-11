chuoi_nhap = input("Nhập chuỗi: ")

ky_tu_dac_biet = ''.join(filter(lambda ky_tu: not ky_tu.isalnum(), chuoi_nhap))

if ky_tu_dac_biet:
    tong_so_ky_tu = len(chuoi_nhap)
    dem_ky_tu_dac_biet = {ky_tu: ky_tu_dac_biet.count(ky_tu) for ky_tu in ky_tu_dac_biet}

    print("Số lần xuất hiện của từng ký tự đặc biệt trong chuỗi:")
    for ky_tu, dem in dem_ky_tu_dac_biet.items():
        ti_le = (dem / tong_so_ky_tu) * 100
        print(f"'{ky_tu}': {dem} lần xuất hiện - Tỷ lệ: {ti_le:.2f}%")
else:
    print("Chuỗi không chứa ký tự đặc biệt.")
