import numpy as np
import matplotlib.pyplot as plt

# Creating an array of x values from -2π to 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Computing (sin) values
y_sin = np.sin(x)
y_rsin = np.sin(x)*2 + 0

# Plotting the two equations
plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label='y=sin(x)', color='blue')
plt.plot(x, y_rsin, label='y_r=2*sin(x) + 0', color='orange')

# labels and lims
plt.xlabel('x')
plt.ylabel('y(x)')

plt.ylim(-2.05, 2.05)
plt.xlim(-6.35,6.35)

# Adding grid and legend
plt.grid(True)
plt.legend()

# Showing the plot
plt.show()
