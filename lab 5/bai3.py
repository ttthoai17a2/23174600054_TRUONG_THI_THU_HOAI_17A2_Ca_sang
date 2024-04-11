chuoi_van_ban = input("Nhập chuỗi văn bản: ")
tu_can_tim = input("Nhập từ cần tìm kiếm: ")
vi_tri = []
vi_tri_bat_dau = -1
while True:
    vi_tri_bat_dau = chuoi_van_ban.find(tu_can_tim, vi_tri_bat_dau + 1)
    if vi_tri_bat_dau == -1:
        break
    vi_tri.append(vi_tri_bat_dau)

if vi_tri:
    print("Vị trí (index) của từ '{}' trong chuỗi là:".format(tu_can_tim), vi_tri)
else:
    print("Từ '{}' không xuất hiện trong chuỗi.".format(tu_can_tim))

dem_tu = {}
for tu in chuoi_van_ban.split():
    if tu in dem_tu:
        dem_tu[tu] += 1
    else:
        dem_tu[tu] = 1

tu_xuat_hien_nhieu_nhat = None
so_lan_xuat_hien_nhieu_nhat = 0
for tu, so_lan in dem_tu.items():
    if so_lan > so_lan_xuat_hien_nhieu_nhat:
        tu_xuat_hien_nhieu_nhat = tu
        so_lan_xuat_hien_nhieu_nhat = so_lan

print("Từ xuất hiện nhiều nhất trong chuỗi là '{}' với số lần xuất hiện là {}.".format(tu_xuat_hien_nhieu_nhat, so_lan_xuat_hien_nhieu_nhat))
