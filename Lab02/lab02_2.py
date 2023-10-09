import math

a = [int(s) for s in input("Please enter numbers separated by a comma:").split(',')]
ans = []
for i in a:
    if i > 0:
        r = math.sqrt((3 * 70 * i) / 25)
        ans.append(str(r))
    else:
        ans.append('Invalid input')
print(ans)