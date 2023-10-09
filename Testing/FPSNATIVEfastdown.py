import matplotlib.pyplot as plt

# Raw time data
times = ["00:00.000.000", "00:00.000.575", "00:01.010.997", "00:02.023.555", "00:03.030.969", 
         "00:04.038.106", "00:05.043.060", "00:06.050.029", "00:07.056.836", "00:08.062.023", 
         "00:09.069.523", "00:10.075.722", "00:11.083.631", "00:12.091.542", "00:13.095.072", 
         "00:14.098.532", "00:15.105.969", "00:16.113.398", "00:17.117.822", "00:18.125.524"]

# Frames Per Second (FPS)
fps = [0, 0, 0, 0, 0, 23, 60, 60, 60, 60, 55, 60, 60, 60, 60, 60, 14, 4, 0, 0]

# Convert time strings to seconds from the start
seconds_from_start = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                       int(t.split(".")[1]) / 1000) for t in times]

plt.plot(seconds_from_start, fps)
plt.title("Frames Per Second Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Frames Per Second (FPS)")

plt.gca().yaxis.grid(True)
plt.show()
