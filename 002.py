a = 1
b = 2
c = 0
d = 0
while b <= 400000:
    if a % 2 == 0:
        d += a
    if b % 2 == 0:
        d += b
    c = a + b
    a = b
    b = c
print d
# Test