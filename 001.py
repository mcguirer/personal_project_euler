x = 0
y = 0
while x < 1000:
    if x % 3 == 0:
        y += x
    else:
        if x % 5 == 0:
            y += x
    x += 1
print y