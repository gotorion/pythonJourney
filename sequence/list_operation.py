lst = list('12345')
lst.append('6')
print(lst)

lst.remove('2')
print(lst)
print(id(lst))

lst.clear();
print(lst)
print(id(lst))

lst.reverse()
print(lst)
print(id(lst))

new_lst = lst.copy()
print(id(new_lst)) # different address
print(id(lst))

lst = ['hello', 'world']
lst[1] = 'mysql'
print(lst)

# sort
nums = [1, 2, 43, 39 ,45]
nums.sort() # based on original list, do not generate new list
print(nums)
nums.sort(reverse=True)
print(nums)
# build in sorted, will create a new list object
new_nums = sorted(nums, reverse=False)
print(new_nums)

if (id(new_nums) != id(nums)):
    print("Different address!")