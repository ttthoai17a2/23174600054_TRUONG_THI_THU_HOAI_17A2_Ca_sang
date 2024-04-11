str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")

do_dai = min(len(str1), len(str2))
chuoi = ""

for i in range(do_dai):
    if str1[i] == str2[i]:
        chuoi += str1[i]
    else:
        break

if len(chuoi) == 0:
    print("Không có chuỗi con chung nào.")
else:
    print("Chuỗi ký tự con chung ngắn nhất:", chuoi)
