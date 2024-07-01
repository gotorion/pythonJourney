def test01():
    lst = [1, 2, 3, 4, 5] 
    print(lst)
test01()

def test02():
    lst = [item * item for item in range(1, 11)]
    print(lst)
test02()

#def test03():
#    lst = [random.randint(1, 100) for _ in range(10)]
#    print(lst)
#test03()

def test04():
    lst = [i for i in range(10) if i % 2 == 0]
    print(lst)
test04()