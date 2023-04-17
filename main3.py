import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('file.csv', delimiter=',')
matrix = np.array(data)
print(matrix)
# # построение графика
# plt.plot(data)
#
# # название графика и обозначение осей
# plt.title('Название графика')
# plt.xlabel('Ось X')
# plt.ylabel('Ось Y')
#
# # рассчет среднеквадратичного отклонения
# stddev = np.std(data)
#
# # вывод значения среднеквадратичного отклонения на график
# plt.text(0.5, 0.9, f'СКО = {stddev:.2f}', ha='center', va='center', transform=plt.gca().transAxes)
#
# # сохранение графика в формате jpeg
# plt.savefig('plot.jpg')
#
# # отображение графика
# plt.show()