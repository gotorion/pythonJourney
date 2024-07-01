t = ('hello', [10, 20, 30], 'python', 20)
print(t)

t = tuple('helloworld')
print(t)

t = tuple([10, 20, 30, 40])
print(t)

if 10 in t:
    print("10 in t")

print(len(t))
print(t.index(20))
print('max =', max(t))
print('min =', min(t))
print(type(t))

del t
print(t) # error