s = input("Input a word to test if it is a palindrome: ")
ans = False
if s[::-1] == s:
    ans = True
print(ans)