import matplotlib.pyplot as plt

# Raw time data
times = [ "00:01.004.860", "00:02.013.803", "00:03.025.665", "00:04.033.982",
         "00:05.045.291", "00:06.052.613", "00:07.062.357", "00:08.068.899", "00:09.081.093",
         "00:10.094.457", "00:11.101.273", "00:12.112.673", "00:13.122.160", "00:14.134.379",
         "00:15.149.226", "00:16.157.932", "00:17.171.409", "00:18.183.006", "00:19.196.990",
         "00:20.212.725", "00:21.223.149", "00:22.231.783", "00:23.243.034", "00:24.250.380",
         "00:25.264.819", "00:26.274.778", "00:27.287.024", "00:28.299.152", "00:29.309.113",
         "00:30.318.608", "00:31.330.834", "00:32.335.204", "00:33.342.247", "00:34.351.034",
         "00:35.358.229", "00:36.365.462", "00:37.372.356", "00:38.378.862", "00:39.385.336",
         "00:40.391.712"]

# Calculate seconds from start
seconds_from_start = [int(t.split(":")[0]) * 60 + float(t.split(":")[1].split(".")[0]) + float(t.split(":")[1].split(".")[1])/1000 + float(t.split(":")[1].split(".")[2])/1000000 for t in times]


# Frames Per Second
fps = [ 40, 6, 34, 60, 60, 60, 60, 44, 60, 60, 60, 60, 60, 60, 36, 60, 56, 37, 60,
       49, 60, 60, 60, 60, 60, 60, 35, 60, 46, 60, 60, 60, 60, 60, 42, 56, 60, 60, 60, 33]

print(f'Length of seconds_from_start: {len(seconds_from_start)}')
print(f'Length of fps: {len(fps)}')

# Check if both lists are of the same length
assert len(seconds_from_start) == len(fps), "The lists must be of the same length."

plt.scatter(seconds_from_start, fps)
plt.title("Frames Per Second (FPS) Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("FPS")

plt.gca().yaxis.grid(True)
plt.show()
