def sum_of_divisors(n):
    divisors_sum = 1  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def amicable(a, b):
    return sum_of_divisors(a) == b and sum_of_divisors(b) == a

a=int(input("Nhập vào một số:"))
b=int(input("Nhập vào một số:"))

if amicable(a, b):
    print(f"{a} và {b} là một cặp số amicable .")
else:
    print(f"{a} và {b} không phải là một cặp số amicable")
