import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
data = pd.read_csv("D:\\pendulumSimulator\\pendulumData\\angleGrid.csv")

# Extract the x and y data from the first row of the DataFrame
x = data.iloc[:, 0].values  # Theta1 values
y = data.iloc[:, 1].values  # Theta2 values

# Create the scatter plot
plt.scatter(x, y)
plt.xlabel('Theta1 (degrees)')
plt.ylabel('Theta2 (degrees)')
plt.title('Scatter plot of initial angles')
plt.grid(True)

# padding stuff
xmin, xmax = np.min(x), np.max(x)
ymin, ymax = np.min(y), np.max(y)
xrange = xmax - xmin
yrange = ymax - ymin
padding = 0.1

# Set the limits of the plot
plt.xlim(xmin - xrange * padding, xmax + xrange * padding)
plt.ylim(ymin - yrange * padding, ymax + yrange * padding)


# Create the scatter plot
plt.scatter(x, y)

# Display the plot
plt.show()
