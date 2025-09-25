import numpy as np
import matplotlib.pyplot as plt

# Creating an array of x values from -2π to 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Computing y values
y_sin = np.sin(x)
y_r1 = np.sin(x)*0.5 + 0.5
y_r2 = np.sin(x)*0.5 - 0.5
y_r3 = np.sin(x)*0.5 + 0

# Creating the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.plot(x, y_r1, label='sin(x) + 0.5', color='red')
plt.plot(x, y_r2, label='sin(x) - 0.5', color='green')
plt.plot(x, y_r3, label='0.5*sin(x) + 0', color='orange')

# labels and lims
plt.xlabel('x')
plt.ylabel('y')

plt.ylim(-1.05, 1.05)
plt.xlim(-6.35,6.35)

# Adding grid and legend
plt.grid(True)
plt.legend()

# Showing the plot
plt.show()
