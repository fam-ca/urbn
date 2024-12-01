# библиотека для работы с запросами
import requests

# # получение данных с веб сайта
r = requests.get('https://api.github.com/events')
print(r.content)

# from 200 to 300 - response sent successfully 
print(r.status_code) 

# # получение http заголовок в ответе
print(r.headers)

###################################################
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print('Sum of arrays: ', a+b)
y = np.mean(a)
print('Average value of array a:', y)
print('Norm of vector: ', np.linalg.norm(a))

###################################################
import matplotlib.pyplot as plt
import random
t = [i for i in range(100)]
y = [random.randint(0, 50) for _ in range(100)]

plt.figure()
plt.scatter(t, y)
plt.show()

###################################################
