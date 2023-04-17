import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = np.random.rand(len(x))
y2 = np.random.rand(len(x))
y3 = 1 / y1
y4 = 1 / y2

# Создание изображения с 4 графиками
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
plt.subplots_adjust(wspace=0.3, hspace=0.3)

# График А
axes[0, 0].plot(x, y1, label='График А')
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('Y')
axes[0, 0].grid(True)
axes[0, 0].legend(loc='best')

# График B
axes[0, 1].plot(x, y2, label='График В')
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('Y')
axes[0, 1].grid(True)
axes[0, 1].legend(loc='best')

# График С
axes[1, 0].plot(y1, y3, label='График С')
axes[1, 0].set_xlabel('Y1')
axes[1, 0].set_ylabel('Y3')
axes[1, 0].grid(True)
axes[1, 0].legend(loc='best')

# График D
axes[1, 1].plot(y2, y4, label='График D')
axes[1, 1].set_xlabel('Y2')
axes[1, 1].set_ylabel('Y4')
axes[1, 1].grid(True)
axes[1, 1].legend(loc='best')

plt.show()

