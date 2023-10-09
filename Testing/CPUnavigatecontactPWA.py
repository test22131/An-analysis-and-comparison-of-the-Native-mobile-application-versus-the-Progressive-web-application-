import matplotlib.pyplot as plt

# Start times
times = ["00:01.011.234", "00:02.024.251", "00:03.067.971", "00:04.073.837", "00:05.137.066",
         "00:06.171.755", "00:07.171.331", "00:08.172.161", "00:09.173.135", "00:10.207.343", 
         "00:11.266.486", "00:12.309.710", "00:13.312.805", "00:14.317.324", "00:15.345.155", 
         "00:16.351.247", "00:17.388.320", "00:18.409.315", "00:19.409.692", "00:20.417.184", 
         "00:21.418.400", "00:22.421.355"]

# Total Load %
total_loads = [48.5, 102.2, 119.5, 162.5, 151.2, 154.7, 152.4, 172.3, 143.5, 158.0,
               164.8, 218.9, 173.1, 117.9, 117.4, 122.6, 118.1, 117.7, 121.5, 120.8, 
               116.3, 121.7]

# Convert start times to seconds from the start
seconds_from_start = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) +
                      int(t.split(".")[1]) / 1000) for t in times]

plt.plot(seconds_from_start, total_loads)
plt.title("Total CPU Load % Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Total CPU Load %")

plt.gca().yaxis.grid(True)
plt.show()
