'''
Viết chương trình Python để tính chỉ số BMI (Body Mass Index) dựa trên chiều
cao và cân nặng được nhập từ người dùng. Chỉ số BMI được tính bằng cách
chia cân nặng (kg) cho bình phương chiều cao (mét). Sau đó, in kết quả chỉ số
BMI và phân loại BMI ra màn hình.
Chương trình sẽ phân loại chỉ số BMI như sau:
+ Nếu chỉ số BMI nhỏ hơn 18.5, sẽ hiển thị phân loại "Gầy".
+ Nếu chỉ số BMI từ 18.5 đến 24.9, sẽ hiển thị phân loại "Bình thường".
+ Nếu chỉ số BMI từ 25.0 đến 29.9, sẽ hiển thị phân loại "Hơi béo".
+ Nếu chỉ số BMI lớn hơn hoặc bằng 30.0, sẽ hiển thị phân loại "Béo".'''

c_c,c_n=map(int,input("Nhập:").split())
bmi=c_n / (c_c ** 2)
if bmi < 18.5:
        print("Gầy",bmi)     
elif 18.5 <= bmi < 25.0:
        print("Bình thường",bmi)
elif 25.0 <= bmi < 30.0:
        print ("Hơi béo",bmi)
else:
        print( "Béo",bmi)
