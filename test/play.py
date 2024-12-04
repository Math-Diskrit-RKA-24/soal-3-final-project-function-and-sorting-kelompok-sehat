def batasan(x):
    y = 0
    z = 0
    for x in str(x):
        y += int(x)
    
    for y in str(y):
        z += int(y)
    return z

masukan = list(map(int, input().split()))
masukan.sort()
masukan.sort(key=lambda x: len(str(x)))
masukan.sort(key=batasan)

for i in masukan:
    print(i, end=" ")