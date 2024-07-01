two_demension_list = [['hello', 'world'], ['hello', 'python']]
for rows in two_demension_list:
    for elem in rows:
        print(elem, end='\t')
    print()

lst = [ [j for j in range(5)] for i in range(4)]
print(lst)