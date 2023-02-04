num = int(input())
dig = []
sum = 0

for i in (str(num)):
    dig.append(int(i))

for i in range(len(dig)):
    sum = sum + dig[i]

print(dig)
print(sum)