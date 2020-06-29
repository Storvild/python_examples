import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

# Создания пространства (fig) и 4х осей
fig, ax = plt.subplots(nrows=2, ncols=2)

fig.subplots_adjust(wspace = 0.4, hspace = 0.6, left = 0.1, right = 0.95, top = 0.9, bottom = 0.1)

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
ax[0,0].plot(t, s)
ax[0,0].set(xlabel='Время (с)', ylabel='Вольтаж (mV)', title='График (plot)')
ax[0,0].grid()

ax[1,0].plot([1, 2, 5, 6, 7, 8], [10, 20, 15, 17, 20, 13], 'o-')

ax[1,1].plot(range(10), [x**2 for x in range(10)], '.-')

ax[0,1].set(title='Отдельные точки (scatter)')
ax[0,1].scatter(10, 20)
ax[0,1].scatter(15, 35)
ax[0,1].scatter(20, 50)
ax[0,1].scatter(30, 30)


# Сохранение видимого графика в файл
# fig.savefig(os.path.join(os.path.abspath(os.path.dirname(__file__)), "test2.png"))
plt.show()

