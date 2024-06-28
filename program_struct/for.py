for ch in 'Hello':
    print(ch)
    
for i in range(1, 11): # start from 1, do not contain 11
    print(i, sep=' ', end=' ')
print()

s = 0
for i in range(1, 11):
    s += i
else:
    print('sum =', s)