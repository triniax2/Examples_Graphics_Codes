import numpy as np
import matplotlib.pyplot as plt

# Two define for the two linear equations
def equation_1(x):
    return 3 * x + 6

def equation_2(x):
    return 6 * x + 0

# To generate x values
x = np.linspace(-10, 10, 100)


# To calculate "y" values for both equations
y1 = equation_1(x)
y2 = equation_2(x)


# Creating the plot
plt.figure(figsize=(8, 6))


# Plotting the two equations
plt.plot(x, y1, label=r'$y(x) = 3x + 6$', color='blue', linewidth=2)
plt.plot(x, y2, label=r'$yr(x) = 6x + 0$', color='orange', linewidth=2)


# Adding labels 
plt.xlabel('x')
plt.ylabel('y(x)')

# plt y-axis range
plt.ylim(-100, 100)

# Adding a legend
plt.legend()

# Showing the grid
plt.grid(True)

# Displaying the plot
plt.show()
