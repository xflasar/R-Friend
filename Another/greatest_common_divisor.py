def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

print(greatest_common_divisor(0, 5))