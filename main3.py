import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel(r'C:\Users\user\Downloads\dataMatplotlib.xlsx', usecols=['X', 'Y'])

x = [float(el) for el in data['X']]
y = [float(el) for el in data['Y']]
plt.xlabel('Ось "Х"')
plt.ylabel('Ось "У"')
plt.title('Электроны в плазме')
plt.plot(x, y)
plt.savefig('Electrons.jpeg')
plt.show()

npx = np.array(x).std()
npy = np.array(y).std()
print(npx, npy)