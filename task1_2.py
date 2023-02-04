line = input()
a = list(line)
print(a)
check=0

for i in range(len(a)):
    for j in range(len(a)):
        if (i!=j) and (a[i] == a[j]):
            check=1

if check==1:
    print('duplicates')
else:
    print('no duplicates')