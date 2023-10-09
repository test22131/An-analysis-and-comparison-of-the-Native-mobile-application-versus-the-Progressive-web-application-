import matplotlib.pyplot as plt

# Raw start time data
times = ["00:00.000.000", "00:00.343.042", "00:01.346.938", "00:02.366.147", "00:03.374.059", 
               "00:04.426.318", "00:05.483.760", "00:06.510.705", "00:07.511.347", "00:08.512.889", 
               "00:09.573.267", "00:10.608.912", "00:11.674.062", "00:12.707.047", "00:13.711.644", 
               "00:14.745.401", "00:15.747.786", "00:16.788.337", "00:17.815.357"]

# Total Load %
total_loads = [25, 47.7, 28.4, 74.6, 113.9, 124.5, 184.7, 190.4, 183.4, 189.4, 
               189.4, 185.8, 195.4, 194.8, 181.8, 158.8, 114.2, 177.2, 115.1]

# Convert time strings to seconds from the start
seconds_from_start = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                       int(t.split(".")[1]) / 1000) for t in times]

plt.plot(seconds_from_start, total_loads)
plt.title("Total Load % Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Total Load %")

plt.gca().yaxis.grid(True)
plt.show()
