import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_name = "D:\\pendulumSimulator\\pendulumData\\initialPerturbedAngles.csv"
data = pd.read_csv(file_name)

# Extract the angles and prepare the lists for the scatter plot
x = []
y = []

# Assuming the header format is "pendulum0Theta1,pendulum0Theta2,pendulum1Theta1,pendulum1Theta2,..."
for i in range(0, len(data.columns), 2):
    x.append(data.iloc[0, i])  # Theta1 values
    y.append(data.iloc[0, i+1])  # Theta2 values

# Create the scatter plot
plt.scatter(x, y)
plt.xlabel('Theta1 (degrees)')
plt.ylabel('Theta2 (degrees)')
plt.title('Scatter plot of initial angles')
plt.grid(True)

# Display the plot
plt.show()
