x = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
y = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
t = x.union(y)
print(x)


x = x.difference(y)
print(x)

x = x.symmetric_difference(y)
print(x)
