import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)

y = np.e**(-1/x**2)

plt.plot(x, y)

plt.plot()
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
