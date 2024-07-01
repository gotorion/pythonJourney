t = (i for i in range(1, 10))
print(t)

print(t.__next__())
print(t.__next__()) # this will clear 1 and 2 from generator

# create tuple from generator object
t = tuple(t)
print(t)