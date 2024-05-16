numbers = [1,2,3,4,5]

# Lọc các số lẻ bằng hàm filter
so_le = list(filter(lambda x: x % 2 != 0, numbers))

print("Các số lẻ trong danh sách:", so_le)

# Lọc các số chẵn bằng hàm filter
so_chan = list(filter(lambda x: x % 2 == 0, numbers))

print("Các số chẵn trong danh sách:", so_chan)

# Tạo danh sách lập phương bằng hàm map
lập_phương = list(map(lambda x: x ** 3, numbers))

print("Danh sách lập phương của các phần tử:", lập_phương)

# Lọc các số chẵn và tính lập phương bằng hàm map và filter
lập_phương_của_số_chẵn = list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, numbers)))

print("Danh sách lập phương của các số chẵn:", lập_phương_của_số_chẵn)

# Lọc các số lẻ và tính bình phương bằng hàm map và filter
bình_phương_của_số_lẻ = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))

print("Danh sách bình phương của các số lẻ:", bình_phương_của_số_lẻ)