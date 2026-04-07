a = 10
b = 10
c=12
print(a is b)
print(a is not b)
print(a is c)

#different objects list
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)
print(x == y)
print(x != y)
print(x is not y)

#same reference
p = [1, 2]
a = p
print(p is a)
