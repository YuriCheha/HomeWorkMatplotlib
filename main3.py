import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel(r'C:\Users\user\Downloads\dataMatplotlib.xlsx')

# построение графика
plt.plot(data)

# название графика и обозначение осей
plt.title('Название графика')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# рассчет среднеквадратичного отклонения
stddev = np.std(data)

# вывод значения среднеквадратичного отклонения на график

# сохранение графика в формате jpeg
plt.savefig('plot.jpg')

# отображение графика
plt.show()