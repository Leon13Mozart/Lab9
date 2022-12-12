A = set()
B = set()
C = set()
 
for i in range(25):
    el = int(i) + 1
    A.add(el)
    if el % 3 == 0:
        B.add(el)
    else:
        C.add(el)

print(A)
print(B)
print(C)
