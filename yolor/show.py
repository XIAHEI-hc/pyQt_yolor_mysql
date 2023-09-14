import numpy as np
import pymysql

import matplotlib.pyplot as plt
import matplotlib.animation as animation

conn = pymysql.connect(host='111.230.38.189', user='root', password='@y1a4n7g8ok0', db='timedata')
cursor = conn.cursor()

cursor.execute("SELECT timestamp, x, y FROM sin_wave_with_time")
data = cursor.fetchall()
print(data[:5])

timestamps, x, y = zip(*data)

# Convert timestamps to a numerical format (like seconds from the start) for plotting
time_nums = [(t - timestamps[0]).total_seconds() for t in timestamps]

# Function for updating the plot
def update(num, time_nums, y, line):
    line.set_data(time_nums[:num], y[:num])
    ax.set_xlim(time_nums[0], time_nums[num])
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')
ax.set_ylim(-1, 1)

ani = animation.FuncAnimation(fig, update, len(time_nums), fargs=[time_nums, y, line],
                              interval=100, blit=True)

plt.show()

cursor.close()
conn.close()
