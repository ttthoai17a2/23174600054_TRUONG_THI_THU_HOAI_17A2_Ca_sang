sinh_vien = {}

for i in range(1, 11):
    ten = input(f"Nhập tên của sinh viên thứ {i}: ")
    diem_thi = float(input(f"Nhập điểm thi của sinh viên {ten}: "))
    sinh_vien[ten] = diem_thi

so_luong_loai_hoc_luc = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for ten, diem in sinh_vien.items():
    if diem >= 8.5:
        so_luong_loai_hoc_luc["A"] += 1
    elif diem >= 7.0:
        so_luong_loai_hoc_luc["B"] += 1
    elif diem >= 5.5:
        so_luong_loai_hoc_luc["C"] += 1
    elif diem >= 4.0:
        so_luong_loai_hoc_luc["D"] += 1
    else:
        so_luong_loai_hoc_luc["F"] += 1

print("\nThống kê số lượng sinh viên ở mỗi loại học lực:")
for loai_hoc_luc, so_luong in so_luong_loai_hoc_luc.items():
    print(f"{loai_hoc_luc}: {so_luong} sinh viên")
