import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
import pandas as pd
import csv
import numpy as np

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

fig, ax = plt.subplots()

# Desktop
f = "D:\\pendulumSimulator\\pendulumData\\doublePendulumPerturbationAngles.csv"

df = pd.read_csv(f)

# Pendulums
numPerturbations = 20
numPendulums = numPerturbations + 1
numMasses = numPendulums * 2

theta1Vals = []
theta2Vals = []

for i in range(0, numMasses, 2):
    theta1 = df.iloc[:, i]
    theta2 = df.iloc[:, i + 1]
    theta1Vals.append(theta1)
    theta2Vals.append(theta2)


colors = ['g', 'r', 'c', 'm', 'y', 'k', 'black', 'aqua', 'lime', 'maroon', 'navy', 'olive', 'purple', 'grey', 'silver',
          'teal', 'white', 'orange', 'hotpink', 'aquamarine']


# Plot scatter points for each frame
with writer.saving(fig, "mp4s\\DoublePendulumPerturbationAngles.mp4", dpi=72):
    for frameNum in range(len(theta1Vals[0])):
        if frameNum % 100 == 0:
            print(frameNum)

        # Clear the plot
        plt.cla()

        # Set the colors of all masses
        for i in range(numPendulums):
            color = colors[i % len(colors)]
            ax.scatter(theta1Vals[i][frameNum], theta2Vals[i][frameNum], c=color)

        writer.grab_frame()

writer.finish()
