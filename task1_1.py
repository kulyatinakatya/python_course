def season(num):
    if num in [1, 2, 12]:
        print('winter')
    if num in [3, 4, 5]:
        print('spring')
    if num in [6, 7, 8]:
        print('summer')
    if num in [9, 10, 11]:
        print('autumn')

num = int(input())
season(num)