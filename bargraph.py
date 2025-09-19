import numpy as np  # Importing NumPy library for numerical operations
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting

# Defining the categories (A, B, C, D) for the x-axis
x = np.array(['A', 'B', 'C', 'D'])

# Defining the corresponding values for each category on the y-axis
y = np.array([10, 20, 30, 40])

# Creating a bar graph with categories on the x-axis and values on the y-axis
plt.bar(x, y)

# Adding labels to the x and y axes
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Adding a title to the bar graph
plt.title('Basic Bar Graph')

# Displaying the bar graph
plt.show()