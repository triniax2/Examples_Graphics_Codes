import numpy as np
import matplotlib.pyplot as plt

# Define the two linear equations
def equation_1(x):
    return 0.62*x + 7.520

def equation_2(x):
    return 0.31*x + 7.520


# Generate x values
x = np.linspace(-10, 10, 10)

# Calculating y values for both equations
y1 = equation_1(x)
y2 = equation_2(x)

# Creating the plot
plt.figure(figsize=(8, 6))

# Plotting the two equations
plt.plot(x, y1, label=r'$\hat{y} = 0.62x + 7.520$', color='black', linewidth=2)
plt.plot(x, y2, label=r'$\hat{y_r} = 0.31x + 7.520$', color='purple', linewidth=2)

# Adding labels and lim
plt.xlabel('x')
plt.ylabel('y')

plt.ylim(0, 15)

# Adding a legend
plt.legend()

# # Showing the grid
plt.grid(True)

# # Displaying the plot
plt.show()
