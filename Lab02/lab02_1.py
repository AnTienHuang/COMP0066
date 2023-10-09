ans = []
for i in range(2000, 4001):
    if i % 9 == 0 and i % 2 != 0:
        ans.append(i)
print(ans)
