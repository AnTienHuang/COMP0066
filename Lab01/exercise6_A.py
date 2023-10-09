a, b, c = input('Input 3 numbers delimited by space: ').split()
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a,b,c)