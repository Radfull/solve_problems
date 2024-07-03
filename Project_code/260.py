import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)

y = 1/(1+x) - 2/x + 1/(1-x)

plt.plot(x, y)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
