l1 = [int(s) for s in input("Enter numbers separated by comma:").split(',')]
l2 = [int(s) for s in input("Enter another set of numbers separated by comma:").split(',')]
ans = []
if len(l1) < len(l2):
    l1, l2 = l2, l1
for i in l2:
    if i in l1 and i not in ans:
        ans.append(i)
print(ans)
