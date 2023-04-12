import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FFMpegWriter, PillowWriter
import pandas as pd

# Desktop ffmpeg path
plt.rcParams['animation.ffmpeg_path'] = 'D:\\ffmpeg\\bin\\ffmpeg.exe'

metadata = dict(title='Movie', artist='me')
# writer = PillowWriter(fps=15, metadata=metadata)
writer = FFMpegWriter(fps=60, metadata=metadata)

l, = plt.plot([], [], 'k-')

# Read from csv files
# Desktop
f = "D:\\pendulumSimulator\\pendulumData\\pendulum.csv"

fig, ax = plt.subplots()

colors = ['g', 'r', 'c', 'm', 'y', 'k', 'black', 'aqua', 'lime', 'maroon', 'navy', 'olive', 'purple', 'grey', 'silver',
          'teal', 'white', 'orange', 'hotpink', 'aquamarine']

df = pd.read_csv(f)

# Pivot
pivotx = df.loc[:, "pivotx"][0]
pivoty = df.loc[:, "pivoty"][0]

# Masses
numMasses = 2
massesXVals = []
massesYVals = []

for i in range(numMasses):
    x = df.loc[:, "mx{}".format(i)]
    y = df.loc[:, "my{}".format(i)]
    massesXVals.append(x)
    massesYVals.append(y)

# Original points
mass0 = np.array([massesXVals[0][0], massesYVals[0][0]])
mass1 = np.array([massesXVals[1][0], massesYVals[1][0]])

originalLen = mass1 - mass0
originalLenMag = np.linalg.norm(originalLen)

# print(mass0)
# print(mass1)
# print(originalLen)
# print(np.linalg.norm(originalLen))

# for i in range(1, 590):
#     m0 = np.array([massesXVals[0][i], massesYVals[0][i]])
#     m1 = np.array([massesXVals[1][i], massesYVals[1][i]])
#
#     curLen = m1 - m0
#     curLenMag = np.linalg.norm(curLen)
#     print("Error at timestep: {}: {}" .format(i, curLenMag - originalLenMag))


with writer.saving(fig, "mp4s\\pendulumSimulation.mp4", 200):
    for frameNum in range(len(massesXVals[0])):
        if frameNum % 100 == 0:
            print(frameNum)

        # Pivot to First Mass
        ax.plot([pivotx, massesXVals[0][frameNum]], [pivoty, massesYVals[0][frameNum]], color="blue")

        # The rest of the masses
        for i in range(numMasses - 1):
            ax.plot([massesXVals[i][frameNum], massesXVals[i + 1][frameNum]],
                    [massesYVals[i][frameNum], massesYVals[i + 1][frameNum]], color=colors[i % len(colors)])
            # ax.scatter(massesXVals[i][frameNum], massesYVals[i][frameNum], color=colors[i % len(colors)])
        plt.xlim([pivotx - 3, pivotx + 3])
        plt.ylim([pivoty - 3, pivoty + 3])

        writer.grab_frame()
        plt.cla()
