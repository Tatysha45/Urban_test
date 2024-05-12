# библиотека requests

import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

for post in data:
    print(post)


# библиотека pandas

import pandas as pd

df = pd.read_csv('example_pandas.csv')
print(df.head())
print(f"Количество строк: {df.shape[0]}, Количество столбцов: {df.shape[1]}")



# библиотека numpy
import numpy as np

a = np.array([1, 2, 3, 4, 5])

b = a + 2

c = a * 3

d = a / 2

print("Массив после добавления 2 к каждому элементу:", b)
print("Массив после умножения каждого элемента на 3:", c)
print("Массив после деления каждого элемента на 2:", d)


# библиотека matplotlib

import matplotlib.pyplot as plt

# initializing the data

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

# график
plt.show()
plt.plot(x, y, 'r')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Заголовок графика')
plt.show()

# 2 графика
fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Заголовок')

plt.tight_layout()
plt.show()


# библиотека pillow

from PIL import Image

image = Image.open('myimage.jpg')

image.thumbnail((700, 500))
grayscale_image = image.convert('L')
grayscale_image.save('myimage_grayscale.png')