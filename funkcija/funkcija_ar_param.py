def print_maks(a, b):
    if a > b:
        print(a, 'ir maksimums')
    elif a == b:
        print(a, 'ir vienāds ar', b)
    else:
        print(b, 'ir maksimums')

print_maks(10, 4)

x = 5
y = 7

print_maks(x, y)
