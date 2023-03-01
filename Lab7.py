import numpy as np
import random
import time

import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.animation import FuncAnimation


# Задание 1

numpy_array1 = np.array(np.random.randint(1, 10, 10**6 + 1), int)
numpy_array2 = np.array(np.random.randint(1, 10, 10**6 + 1), int)

standard_array1 = [random.randint(1, 10) for i in range(10**6 + 1)]
standard_array2 = [random.randint(1, 10) for j in range(10**6 + 1)]


#считает произведение двух обычных массивов
result_array = []
for i in range(10**6 + 1):
    result_array.append(standard_array1[i] * standard_array2[i])
print(time.perf_counter())

#считает произведение двух массивов вида Numpy
result_numpy = np.multiply(numpy_array1, numpy_array2)
print(time.perf_counter())


#Задание 2 Вариант 8 (4 столбца)

data = pd.read_csv('data2.csv',
                   sep=',',
                   parse_dates=['ph', 'Hardness', 'Solids', 'Chloramines'])

x1 = list(data['ph'])
x2 = list(data['Hardness'])
x3 = list(data['Solids'])
x4 = list(data['Chloramines'])

colors = ['#E69F00', '#56B4E9', '#F0E442', '#009E73']
names = ['ph', 'Hardness', 'Solids', 'Chloramines']

plt.hist([x1, x2, x3, x4], bins = int(180/15),
         color = colors, label=names)

plt.legend()
plt.xlabel('Time')
plt.ylabel('Normalized Values')
plt.title('I D K')
plt.show()


#Задание 3 (формула: x∈(-3п;3п); y=cos(x); z=x/sin(x))

x = np.linspace(-3 * np.pi, 3 * np.pi, 50)
y = np.cos(x)
z = x / np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='parametric curve')
plt.show()



#Доп задание

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

plt.show()
