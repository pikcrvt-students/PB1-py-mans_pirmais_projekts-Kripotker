sk = int(input())
fakt = 1
reiz = 2
for reiz in range(reiz, sk + 1):
    fakt = reiz * fakt
    reiz = reiz + 1
    
print(fakt)
