import matplotlib.pyplot as plt

# Raw time data
times = ["00:00.000.000", "00:00.000.602", "00:01.013.571", "00:02.022.805", "00:03.031.592", 
         "00:04.037.876", "00:05.045.797", "00:06.053.493", "00:07.061.179", "00:08.068.907",
         "00:09.077.247", "00:10.081.751", "00:11.087.242", "00:12.097.021", "00:13.105.311", 
         "00:14.112.826", "00:15.118.221", "00:16.122.033", "00:17.131.132", "00:18.140.167",
         "00:19.145.385", "00:20.154.175"]

# Frames Per Second (FPS)
fps = [0, 0, 0, 0, 0, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 29, 30, 14]

# Convert time strings to seconds from the start
seconds_from_start = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                       int(t.split(".")[1]) / 1000) for t in times]

plt.plot(seconds_from_start, fps)
plt.title("Frames Per Second Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Frames Per Second (FPS)")

plt.gca().yaxis.grid(True)
plt.show()