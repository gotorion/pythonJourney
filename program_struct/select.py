condition = True
if (condition):
    print(True)
else:
    print(False)
    
num = 10
if num != 8:
    print('actual num =', num)
    
num = eval(input('Input num: '))
if num >= 90:
    print('GREAT')
elif num < 60:
    print('BAD')
else:
    print('WHATEVER')

username = 'john'
password = 'john'
if username == password and condition:
    print('login success')