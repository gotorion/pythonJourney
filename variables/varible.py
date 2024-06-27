value = 10 # 10 in heap, value in stack, value point to 10
print(value)
print(type(value))
value = 'string' # this is ok
print(value)
print(type(value))

num1 = num2 = 1024
print(num1, num2, sep='|')

print(id(num1)) # id means get address of num
print(id(num2))

if value == 'string':
    print(True)
elif value == 10:
    print(value)
else:
    print(False)