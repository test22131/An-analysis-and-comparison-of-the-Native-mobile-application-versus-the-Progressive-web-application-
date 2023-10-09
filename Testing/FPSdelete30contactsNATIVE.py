import matplotlib.pyplot as plt

# Raw time data
times = ["00:02.026.158", "00:03.040.326", "00:04.048.750", "00:05.057.137", "00:06.061.572", 
             "00:07.069.926", "00:08.077.067", "00:09.084.999", "00:10.091.807", "00:11.099.645", 
             "00:12.107.942", "00:13.117.661", "00:14.121.904", "00:15.127.336", "00:16.137.645", 
             "00:17.144.160", "00:18.153.756", "00:19.162.551", "00:20.171.319"]

# Frames Per Second (FPS)
fps = [0, 0, 0, 6, 21, 22, 24, 25, 23, 26, 20, 18, 22, 26, 19, 21, 25, 0, 0]

# Convert time strings to seconds from the start
seconds_from_start = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                       int(t.split(".")[1]) / 1000) for t in times]

plt.plot(seconds_from_start, fps)
plt.title("Frames Per Second Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Frames Per Second (FPS)")

plt.gca().yaxis.grid(True)
plt.show()
