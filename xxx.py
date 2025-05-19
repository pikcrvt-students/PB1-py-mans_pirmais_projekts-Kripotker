s = -3.0
e = 1.2
ss = 0.2

for i in range(int((e - s) / ss)):
    x = s + i * ss
    y = x * x 
    print(f"x = {x}, y = {y}")
