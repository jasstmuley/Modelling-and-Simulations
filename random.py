from random import randint
import matplotlib.pyplot as plt

value = {}
for _ in range(2000):
    x = randint(0,10)
    if str(x) in value:
        value[str(x)] += 1
    else:
        value[str(x)] = 1
x = []
y = []
b = 0
for temp in value:
    x.append(value[temp])
    y.append(b)
    b += 1


# We can set the number of bins with the `bins` kwarg
plt.plot(x,'bo')
plt.ylim((0,400))

