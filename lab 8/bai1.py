def la_so_nguyen_to(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to_sinh_doi(gioi_han):
    for i in range(3, gioi_han, 2):
        if la_so_nguyen_to(i) and la_so_nguyen_to(i + 2):
            print(f"({i}, {i + 2})")

tim_so_nguyen_to_sinh_doi(1000)
