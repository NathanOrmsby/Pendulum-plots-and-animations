import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
data = pd.read_csv("D:\\pendulumSimulator\\pendulumData\\lyapunovPendulumSystems.csv")

# Extract the x and y data from the first row of the DataFrame
resolution = [20, 20]
numBasePendulums = resolution[0] * resolution[1]

# Collect the base pendulum angle values

baseTheta1 = data.iloc[:numBasePendulums, 0].values  # Theta1 values
baseTheta2 = data.iloc[:numBasePendulums, 1].values  # Theta2 values

perturbedTheta1 = data.iloc[numBasePendulums:, 0].values  # Theta1 values
perturbedTheta2 = data.iloc[numBasePendulums:, 1].values  # Theta2 values

# Base pendulums
plt.scatter(baseTheta1, baseTheta2, c="blue", s=10)
# Perturbed pendulums
plt.scatter(perturbedTheta1, perturbedTheta2, c="red", s=10)

plt.xlabel('Theta1 (degrees)')
plt.ylabel('Theta2 (degrees)')
plt.title('Scatter plot of initial angles')
plt.grid(True)

# padding stuff
xmin = min(min(a, b) for a, b in zip(baseTheta1, perturbedTheta1))
xmax = max(max(a, b) for a, b in zip(baseTheta1, perturbedTheta1))
ymin = min(min(a, b) for a, b in zip(baseTheta2, perturbedTheta2))
ymax = max(max(a, b) for a, b in zip(baseTheta2, perturbedTheta2))

xrange = xmax - xmin
yrange = ymax - ymin
padding = 0.1

# Set the limits of the plot
# plt.xlim(xmin - xrange * padding, xmax + xrange * padding)
# plt.ylim(ymin - yrange * padding, ymax + yrange * padding)

# Display the plot
plt.show()
