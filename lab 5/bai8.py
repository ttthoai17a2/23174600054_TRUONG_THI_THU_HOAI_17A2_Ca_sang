s = input("Nhập chuỗi (ít nhất 11 ký tự): ")

if len(s) < 11:
    print("Chuỗi phải có ít nhất 11 ký tự.")
else:
    # a) Trích ra chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8.
    sub_a = s[1:8]
    print("Chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8:", sub_a)

    # b) Trích ra chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5.
    sub_b = s[4:9]
    print("Chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5:", sub_b)

    # c) Trích ra chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự.
    sub_c = s[-3:]
    print("Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", sub_c)

    # d) Chuyển đổi các ký tự trong chuỗi thành chữ thường.
    lower = s.lower()
    print("Chuỗi sau khi chuyển đổi thành chữ thường:", lower)

    # e) Chuyển đổi các ký tự trong chuỗi thành chữ hoa.
    upper = s.upper()
    print("Chuỗi sau khi chuyển đổi thành chữ hoa:", upper)

    # f) Đảo ngược chuỗi ký tự vừa nhập.
    dao_ngược = s[::-1]
    print("Chuỗi sau khi đảo ngược:", dao_ngược)
