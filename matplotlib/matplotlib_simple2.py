import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='Время (с)', ylabel='Вольтаж (mV)',
       title='Заголовок графика')
ax.grid()

ax2 = ax.twinx()
#ax2.axis([-0.04, 3.6, 0.0, 800.0])

# Сохранение видимого графика в файл
# fig.savefig(os.path.join(os.path.abspath(os.path.dirname(__file__)), "test2.png"))
plt.show()

