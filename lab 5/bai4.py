s = input("Nhập chuỗi ký tự: ")
number_string = ''.join(char for char in s if char.isdigit())

if number_string:
    number = int(number_string)

    # Kiểm tra xem số nguyên đó có phải là số nguyên tố không
    if number <= 1:
        check = False
    else:
        check = True
        i = 2
        while i * i <= number:
            if number % i == 0:
                check = False
                break
            i += 1

    if check:
        print("Chuỗi ký tự sau khi loại bỏ và kiểm tra là một số nguyên tố.")
    else:
        print("Chuỗi ký tự sau khi loại bỏ và kiểm tra không phải là một số nguyên tố.")
else:
    print("Chuỗi không chứa số nguyên nào.")
