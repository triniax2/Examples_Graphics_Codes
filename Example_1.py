import numpy as np
import matplotlib.pyplot as plt

# Two define for the two linear equations
def equation_1(x):
    return 4 * x + 2

def equation_2(x):
    return 2 * x


# To generate x values
x = np.linspace(-10, 10, 100)


# To calculate "y" values for both equations
y1 = equation_1(x)
y2 = equation_2(x)

# Creating the plot
plt.figure(figsize=(8, 6))

# Plotting the two equations
plt.plot(x, y1, label=r'$y = 4x + 2$', color='blue', linewidth=2)
plt.plot(x, y2, label=r'$yr = 2x$', color='green', linewidth=2)

# Adding labels and title
plt.xlabel('x')
plt.ylabel('y')

# plt.title('Plot of Two Linear Equations')
plt.ylim(-40, 40)

# Adding a legend
plt.legend()

# Showing the grid
plt.grid(True)

# Displaying the plot
plt.show()
