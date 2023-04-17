import matplotlib.pyplot as plt
import numpy as np

m = np.linspace(0, 10, 11)
c = 299792458
E = m * (c ** 2)
plt.plot(m, E)
plt.title('Зависимость Энергии от массы')
plt.xlabel('Масса, г')
plt.ylabel('Энергия, Дж')
plt.savefig('Energy.svg')
plt.show()