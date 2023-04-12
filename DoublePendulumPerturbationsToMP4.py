import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
import pandas as pd

# Desktop ffmpeg path
plt.rcParams['animation.ffmpeg_path'] = 'C:\\ProgramData\\chocolatey\\bin\\ffmpeg.exe'

metadata = dict(title='Movie', artist='me')

# This shit doesn't work
extra_args = [
    "-c:v", "h264_nvenc",  # Use NVIDIA h264_nvenc codec
    "-preset", "fast",  # Use fast preset for the h264_nvenc codec
    "-pix_fmt", "yuv420p",  # Select pixel format
    "-metadata", "title=Movie",
    "-metadata", "artist=me",
    "-threads", "0",  # Use maximum available threads
]

writer = FFMpegWriter(fps=60, metadata=metadata, extra_args=extra_args)

l, = plt.plot([], [], 'k-')

# Read from csv files
# Desktop
f = "D:\\pendulumSimulator\\pendulumData\\doublePendulumPerturbations.csv"

fig, ax = plt.subplots()

colors = ['g', 'r', 'c', 'm', 'y', 'k', 'black', 'aqua', 'lime', 'maroon', 'navy', 'olive', 'purple', 'grey', 'silver',
          'teal', 'white', 'orange', 'hotpink', 'aquamarine']

df = pd.read_csv(f)

# Pivot
pivotx = 0
pivoty = 0

# Pendulums
numPerturbations = 20
numPendulums = numPerturbations + 1
numMasses = numPendulums * 2
massesXVals = []
massesYVals = []

for i in range(numMasses):
    x = df.loc[:, "m{}x".format(i)]
    y = df.loc[:, "m{}y".format(i)]
    massesXVals.append(x)
    massesYVals.append(y)

lines = []
for i in range(numPendulums):
    line1, = ax.plot([], [], color=colors[i % len(colors)])
    line2, = ax.plot([], [], color=colors[i % len(colors)])
    lines.append((line1, line2))

pivot_line, = ax.plot([], [], color="blue")  # Create a line object for the pivot point
with writer.saving(fig, "mp4s\\DoublePendulumPerturbations.mp4", dpi=200):
    for frameNum in range(len(massesXVals[0])):
        if frameNum % 100 == 0:
            print(frameNum)

        # The rest of the masses
        for i in range(numPendulums):
            line1, line2 = lines[i]

            # Update line data
            line1.set_data([pivotx, massesXVals[2 * i][frameNum]], [pivoty, massesYVals[2 * i][frameNum]])
            line1.set_color(colors[i % len(colors)])  # Set the color of the pivot to first mass line
            line2.set_data([massesXVals[2 * i][frameNum], massesXVals[2 * i + 1][frameNum]],
                           [massesYVals[2 * i][frameNum], massesYVals[2 * i + 1][frameNum]])

        plt.xlim([pivotx - 3, pivotx + 3])
        plt.ylim([pivoty - 3, pivoty + 3])

        writer.grab_frame()
        # Remove plt.cla() since we are updating line objects

writer.finish()