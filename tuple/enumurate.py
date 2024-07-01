t = tuple([10, 20, 30, 40])
strs = ('python', 'hello', 'world')
print(strs[0])

str2 = strs[0:3:2]
print(str2)

for item in strs:
    print(item)
    
for index, item in enumerate(t, start=1):
    print(index, '---->', item)