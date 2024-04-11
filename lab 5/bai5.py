str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")

chuoi = ""
len1 = len(str1)
len2 = len(str2)
do_dai = max(len1, len2)

for i in range(do_dai):
    if i < len1:
        chuoi += str1[i] + "-"
    if i < len2:
        chuoi += str2[i] + "-"

# Loại bỏ dấu gạch nối cuối cùng
if chuoi.endswith("-"):
    chuoi= chuoi[:-1]

print("Chuỗi kết quả sau khi trộn là:",chuoi)

