#Viết chương trình nhập vào một số nguyên có ba chữ số từ người dùng. Hãy in
#ra cách đọc của số nguyên này theo tiếng Anh.
n = int(input("Nhập vào số nguyên n: "))
if 100 <= n <= 999:
    chu_so_hang_tram = n // 100
    chu_so_hang_chuc = (n//10) % 10
    chu_so_hang_don_vi = n % 10
    # Đọc chữ số hàng trăm
    if chu_so_hang_tram == 1:
        doc_hang_tram = "one hundred"                         
    elif chu_so_hang_tram == 2:
        doc_hang_tram = 'two hundred'
    elif chu_so_hang_tram == 3:                                                                           
        doc_hang_tram = 'three hundred'
    elif chu_so_hang_tram == 4:
        doc_hang_tram = 'four hundred'
    elif chu_so_hang_tram == 5:
        doc_hang_tram = 'five hundred'
    elif chu_so_hang_tram== 6:
        doc_hang_tram = 'six hundred'
    elif chu_so_hang_tram == 7:
        doc_hang_tram = 'seven hundred'
    elif chu_so_hang_tram == 8:
        doc_hang_tram = 'eight hundred'
    elif chu_so_hang_tram == 9:
        doc_hang_tram = 'nine hundred'
    elif chu_so_hang_tram == 0:
        doc_hang_tram = ''
    # Đọc chữ số hàng chục
    if chu_so_hang_chuc == 1:
        doc_hang_chuc = "ten"
    elif chu_so_hang_chuc == 2:
        doc_hang_chuc = 'twenty'
    elif chu_so_hang_chuc == 3:
        doc_hang_chuc = 'thirty'
    elif chu_so_hang_chuc == 4:
        doc_hang_chuc = 'forty'
    elif chu_so_hang_chuc == 5:
        doc_hang_chuc = 'fifty'
    elif chu_so_hang_chuc == 6:
        doc_hang_chuc = 'sixty'
    elif chu_so_hang_chuc == 7:
        doc_hang_chuc = 'seventy'
    elif chu_so_hang_chuc == 8:
        doc_hang_chuc = 'eighty'
    elif chu_so_hang_chuc == 9:
        doc_hang_chuc = 'ninety'
    elif chu_so_hang_chuc == 0:
        doc_hang_chuc = ''
    # Đọc chữ số hàng đơn vị
    if chu_so_hang_don_vi == 1:
        doc_hang_don_vi = "one"
    elif chu_so_hang_don_vi == 2:
        doc_hang_don_vi = 'two'
    elif chu_so_hang_don_vi == 3:
        doc_hang_don_vi = 'three'
    elif chu_so_hang_don_vi == 4:
        doc_hang_don_vi = 'four'
    elif chu_so_hang_don_vi == 5:
        doc_hang_don_vi = 'five'
    elif chu_so_hang_don_vi == 6:
        doc_hang_don_vi = 'six'
    elif chu_so_hang_don_vi == 7:
        doc_hang_don_vi = 'seven'
    elif chu_so_hang_don_vi == 8:
        doc_hang_don_vi = 'eight'
    elif chu_so_hang_don_vi == 9:
        doc_hang_don_vi = 'nine'
    elif chu_so_hang_don_vi == 0:
        doc_hang_don_vi = ''
    print("Số",n, "đọc là:", doc_hang_tram, doc_hang_chuc, doc_hang_don_vi)