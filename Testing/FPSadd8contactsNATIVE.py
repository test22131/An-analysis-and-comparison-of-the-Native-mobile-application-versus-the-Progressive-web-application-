import matplotlib.pyplot as plt

# Raw time data
times = ["00:00.000.000", "00:00.000.513", "00:01.007.747", "00:02.015.515", "00:03.026.902",
         "00:04.034.529", "00:05.041.899", "00:06.049.234", "00:07.052.597", "00:08.059.947",
         "00:09.067.477", "00:10.071.294", "00:11.079.007", "00:12.086.461", "00:13.093.630",
         "00:14.100.644", "00:15.107.448", "00:16.114.483", "00:17.121.281", "00:18.128.143",
         "00:19.134.946", "00:20.141.477", "00:21.148.338", "00:22.155.370"]

# Frames Per Second (FPS)
fps = [0, 8, 8, 8, 8, 8, 8, 10, 43, 40, 38, 41, 48, 45, 24, 44, 31, 53, 38, 44, 29, 12, 8, 8]

# Convert time strings to seconds from the start
seconds_from_start = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                       int(t.split(".")[1]) / 1000) for t in times]

plt.plot(seconds_from_start, fps)
plt.title("Frames Per Second Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Frames Per Second (FPS)")

plt.gca().yaxis.grid(True)
plt.show()
