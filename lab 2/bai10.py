'''Viết một chương trình Python cho người dùng có thể lựa chọn các thể loại phim
như Hành động, Kinh dị, Tình cảm, Hài hước và Hoạt hình. Sau đó, yêu cầu
người dùng nhập lựa chọn thể loại phim và thời gian muốn xem phim (sáng,
trưa, chiều, tối). Cuối cùng, chương trình sẽ hiển thị thông báo về thời gian
chiếu phim tương ứng với lựa chọn của người dùng. Hãy lưu ý rằng phim Tình
cảm chỉ được chiếu vào buổi tối, phim hoạt hình chỉ được chiếu vào buổi sáng
và trưa, phim kinh dị chỉ được chiếu vào buổi tối. Nếu thời gian chọn không có
suất chiếu, hãy in ra thông báo "Không có suất chiếu”'''

the_loai = input("Chọn thể loại phim : ")
thoi_gian = input("Chọn thời gian xem phim (sáng, trưa, chiều, tối): ")
if the_loai ==  "hành động"or the_loai == "hài hước":
    if thoi_gian == "sáng" or thoi_gian == "trưa" or thoi_gian == "chiều" or thoi_gian == "tối":
        print(f"Thời gian chiếu phim hành động/hài hước: {thoi_gian}")
    else:
        print("Không có suất chiếu!!")
elif the_loai == 'kinh dị':
    if thoi_gian == "tối":
        print(f"Thời gian chiếu phim Kinh dị: {thoi_gian}.")
    else:
        print("Không có suất chiếu cho phim Kinh dị vào buổi sáng, trưa và chiều.")
elif the_loai == 'tình cảm':
    if thoi_gian == "tối":
        print(f"Thời gian chiếu phim Tình cảm: {thoi_gian}.")
    else:
        print("Không có suất chiếu cho phim Tình cảm vào buổi sáng, trưa và chiều.")
elif the_loai == 'hoạt hình':
    if thoi_gian == "sáng" or thoi_gian == "trưa":
        print(f"Thời gian chiếu phim hoạt hình: {thoi_gian}.")
    elif thoi_gian == "chiều" or thoi_gian == "tối":
        print("Không có suất chiếu cho phim Hoạt hình vào buổi chiều và tối.")
    else:
        print("không có suất chiếu nào!!.")
else:
    print("Lựa chọn không hợp lệ.")