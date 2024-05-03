van_ban = "I love my grandparents. My grandfather is a retired officer from army and my grandmother is a retired teacher. I am the star of their eyes. My best time of the day is the bedtime. When they tell me stories. My grandfather also helps me in my studies. I spend most of the time with them. They are the most valuable assets of my life."

tach_tu = van_ban.split()
so_luong_tu = {}
for tu in tach_tu:
    if tu.lower() in so_luong_tu:
        so_luong_tu[tu.lower()] += 1
    else:
        so_luong_tu[tu.lower()] = 1

tu_nhieu_nhat = max(so_luong_tu, key=so_luong_tu.get)
tu_it_nhat = min(so_luong_tu, key=so_luong_tu.get)
print("Từ có số lượng nhiều nhất:", tu_nhieu_nhat, "- Số lượng:", so_luong_tu[tu_nhieu_nhat])
print("Từ có số lượng ít nhất:", tu_it_nhat, "- Số lượng:", so_luong_tu[tu_it_nhat])
