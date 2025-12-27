import numpy as np
import matplotlib.pyplot as plt

# Define the two equations
def equation_1(x):
    return 600 * x + 3000

def equation_2(x):
    return 300 * x + 3000

# x-axis range
x_min = -30
x_max = 30
num_points = 200

# Generate x values
x = np.linspace(x_min, x_max, num_points)

# Calculate y values
y1 = equation_1(x)
y2 = equation_2(x)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the equations
plt.plot(x, y1, label=r'$C_r(x) = 600x + 3000$', color='blue', linewidth=2)
plt.plot(x, y2, label=r'$C_o(x) = 300x + 3000$', color='orange', linewidth=2)

# Labels
plt.xlabel('x')
plt.ylabel('C(x)')

# Axis limits
plt.xlim(x_min, x_max)
plt.ylim(-2000, 6000)

# Legend and grid
plt.legend()
plt.grid(True)

# Show plot
plt.show()
