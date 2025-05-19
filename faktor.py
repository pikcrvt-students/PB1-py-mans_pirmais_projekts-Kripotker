def fakt(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fakt(n - 1)

sk = int(input())
print(fakt(sk))
