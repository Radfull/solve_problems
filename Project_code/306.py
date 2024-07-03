import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 10000)

y_1 = 2**(-x) * np.sqrt(np.sin(np.pi * x))
y_2 = -2**(-x) * np.sqrt(np.sin(np.pi * x))

plt.plot(x, y_1)
plt.plot(x, y_2)
plt.grid(True)

plt.xlabel('x')
plt.ylabel('y')
plt.show()
