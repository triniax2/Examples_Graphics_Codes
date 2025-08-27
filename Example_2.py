import numpy as np
import matplotlib.pyplot as plt

# Two define for the two linear equations
def equation_1(x):
    return 400 * x + 800

def equation_2(x):
    return 200 * x + 800


# To generate x values
x = np.linspace(-90, 90, 100)


# To calculate "y" values for both equations
y1 = equation_1(x)
y2 = equation_2(x)

# Creating the plot
plt.figure(figsize=(8, 6))

# Plotting the two equations
plt.plot(x, y1, label=r'$c(x) = 400x + 800$', color='brown', linewidth=2)
plt.plot(x, y2, label=r'$c(x)r = 200x + 800$', color='orange', linewidth=2)

# Adding labels and title
plt.xlabel('x')
plt.ylabel('y')

# plt.title('Plot of Two Linear Equations')

plt.ylim(-10000, 10000)

# Adding a legend
plt.legend()

# Showing the grid
plt.grid(True)

# Displaying the plot
plt.show()