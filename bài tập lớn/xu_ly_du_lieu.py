import csv
import random

def tung_xuc_xac():
    return random.randint(1, 6)

def mo_phong_tro_choi(diem_muc_tieu, tu_dong=False):
    tong_diem = 0
    while True:
        if tu_dong:
            lua_chon = 'c' if random.choice([True, False]) else 'k'
        else:
            lua_chon = input("Bạn có muốn tung xúc xắc không? (c/k): ").strip().lower()
        
        if lua_chon == 'c':
            lan_tung = tung_xuc_xac()
            if not tu_dong:
                print(f"Bạn đã tung được số {lan_tung}.")
            tong_diem += lan_tung
            if not tu_dong:
                print(f"Tổng điểm hiện tại của bạn là {tong_diem}.")
            if tong_diem > diem_muc_tieu:
                if not tu_dong:
                    print("Bạn đã vượt quá điểm số mục tiêu. Bạn thua!")
                return tong_diem, "Thua"
            elif tong_diem == diem_muc_tieu:
                if not tu_dong:
                    print("Bạn đã đạt điểm số mục tiêu. Bạn thắng!")
                return tong_diem, "Thắng"
        elif lua_chon == 'k':
            if not tu_dong:
                print(f"Bạn đã dừng lại với tổng điểm là {tong_diem}.")
            return tong_diem, "Dừng lại"
        else:
            if not tu_dong:
                print("Lựa chọn không hợp lệ. Vui lòng nhập 'c' hoặc 'k'.")

def tinh_xac_suat_thang(diem_muc_tieu, so_lan_mo_phong=1000):
    so_lan_thang = 0
    for _ in range(so_lan_mo_phong):
        tong_diem, ket_qua = mo_phong_tro_choi(diem_muc_tieu, tu_dong=True)
        if ket_qua == "Thắng":
            so_lan_thang += 1
    return so_lan_thang / so_lan_mo_phong

def main():
    diem_muc_tieu = int(input("Nhập điểm số mục tiêu: "))
    
    ket_qua = []
    
    while True:
        tong_diem, ket_qua_tran = mo_phong_tro_choi(diem_muc_tieu)
        ket_qua.append((tong_diem, ket_qua_tran))
        
        choi_tiep = input("Bạn có muốn chơi lại không? (c/k): ").strip().lower()
        if choi_tiep != 'c':
            break
    
    print("Đang tính xác suất thắng...")
    xac_suat_thang = tinh_xac_suat_thang(diem_muc_tieu)
    print(f"Xác suất thắng là {xac_suat_thang:.2f}")
    
    try:
        with open('ket_qua_tro_choi.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Tổng Điểm", "Kết Quả", "Xác Suất Thắng"])
            for tong_diem, ket_qua_tran in ket_qua:
                writer.writerow([tong_diem, ket_qua_tran, xac_suat_thang])
        print("Kết quả trò chơi đã được lưu vào file ket_qua_tro_choi.csv.")
    except Exception as e:
        print(f"Có lỗi xảy ra khi lưu file CSV: {e}")

if __name__ == "__main__":
    main()