# tuples are comparable
a = (0, 1, 2) < (5, 1, 2)
print(a)
b = (0, 1, 2000000) < (0, 3, 4)
print(b)
c = ('Jones', 'Sally') < ('Jones', 'Sam')
print(b)
d = ('Jones', 'Sally') > ('Adams', 'Sam')
print(d)

# It only compares the first item, so doesn't matter if for ex:
e = (1, 9999999) > (3, 0)
print(e)
# but if both are even, then it goes to the sencond item. For ex:
f = (0, 1) > (0, 2)
print(f)

