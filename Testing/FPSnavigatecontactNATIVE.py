import matplotlib.pyplot as plt

# Raw time data
times = ["00:00.000.000", "00:00.000.391", "00:01.008.299", "00:02.022.400", "00:03.035.794", 
         "00:04.040.984", "00:05.048.732", "00:06.056.766", "00:07.064.728", "00:08.070.448", 
         "00:09.078.899", "00:10.086.987", "00:11.095.633", "00:12.102.826", "00:13.110.844", 
         "00:14.119.410", "00:15.126.870", "00:16.131.175", "00:17.139.451", "00:18.147.148", 
         "00:19.154.945", "00:20.168.485", "00:21.176.431", "00:22.183.660", "00:23.195.521"]

# Frames Per Second (FPS)
fps = [0, 0, 0, 0, 0, 0, 0, 33, 29, 60, 54, 60, 36, 60, 60, 60, 60, 57, 60, 27, 60, 53, 48, 0, 0]

# Convert time strings to seconds from the start
seconds_from_start = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                       int(t.split(".")[1]) / 1000) for t in times]

plt.plot(seconds_from_start, fps)
plt.title("Frames Per Second Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Frames Per Second (FPS)")

plt.gca().yaxis.grid(True)
plt.show()
