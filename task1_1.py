def season(num):
    if num in [1, 2, 12]:
        return('winter')
    if num in [3, 4, 5]:
        return('spring')
    if num in [6, 7, 8]:
        return('summer')
    if num in [9, 10, 11]:
        return('autumn')

num = int(input())
season(num)
