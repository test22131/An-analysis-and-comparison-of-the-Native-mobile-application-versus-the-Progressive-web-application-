import matplotlib.pyplot as plt

# Interval data
intervals = ["00:03.039.883", "00:07.080.693", "00:15.179.969", "00:21.238.924",
             "00:08.092.682", "00:11.136.864", "00:12.146.081", "00:14.171.352",
             "00:04.054.404", "00:06.070.548", "00:09.106.245", "00:10.121.791",
             "00:13.159.785", "00:16.187.376", "00:05.061.995", "00:20.227.284",
             "00:19.214.203"]

# Frames Per Second (FPS)
fps = [12, 16, 9, 13, 9, 23, 11, 16, 15, 15, 17, 21, 14, 13, 13, 9, 30]

# Convert interval data to seconds from the start
seconds_from_start = [float(t.split(".")[0].split(":")[1]) + float(t.split(".")[1]) / 1000 for t in intervals]

plt.scatter(seconds_from_start, fps)
plt.title("Frames Per Second (FPS) Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("FPS")

plt.gca().yaxis.grid(True)
plt.show()
