import numpy as np
import matplotlib.pyplot as plt

# Two define for the two linear equations
def equation_1(x):
    return 4 * x + 2

def equation_2(x):
    return 2 * x + 0

def equation_3(x):
    return 2 * x + 2


# To generate x values
x = np.linspace(-10, 10, 100)


# To calculate "y" values for both equations
y1 = equation_1(x)
y2 = equation_2(x)
y3 = equation_3(x)


# Creating the plot
plt.figure(figsize=(8, 6))

# Plotting the two equations
plt.plot(x, y1, label=r'$y(x) = 4x + 2$', color='blue', linewidth=2)
plt.plot(x, y2, label=r'$yr1(x) = 2x + 0$', color='red', linewidth=2)
plt.plot(x, y3, label=r'$yr2(x) = 2x + 2$', color='green', linewidth=2)


# Adding labels and lim
plt.xlabel('x')
plt.ylabel('y')

plt.ylim(-50, 50)

# Adding a legend
plt.legend()

# Showing the grid
plt.grid(True)

# Displaying the plot
plt.show()
