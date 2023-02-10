str = input()
str_r = ''.join(reversed(str))
print(str_r)

if str == str_r:
    print('is palindrome')
else:
    print('is not a palindrome')