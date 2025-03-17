#Lista de interaveis ate 10
x = [i for i in range(1, 10)]
print(x)

#Lista multiplicando por 2
y = [i * 2 for i in range(1, 10)]
print(y)


#List comprehension
x = [ [j for j in range (4, 7)] for i  in range(0, 3)]
print(x)

#Lista tridimensional

z = [ [[input() for h in range(0,2)] for x in range(0, 2)] for i in range (0,2)]
print(z)
