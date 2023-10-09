import matplotlib.pyplot as plt

# Start times
times = ["00:00.000.000", "00:00.341.968", "00:01.342.690", "00:02.403.346", "00:03.439.155", 
         "00:04.440.197", "00:05.471.649", "00:06.474.324", "00:07.538.207", "00:08.600.443", 
         "00:09.601.966", "00:10.646.900", "00:11.675.766", "00:12.684.693", "00:13.690.113", 
         "00:14.730.346", "00:15.747.747", "00:16.761.404", "00:17.787.661", "00:18.808.236", 
         "00:19.840.444", "00:20.843.532", "00:21.878.676", "00:22.941.463"]

# Total Load %
total_loads = [50, 61.9, 118.7, 72.7, 168.6, 118.9, 118.1, 164.2, 144.3, 179.6, 
               153.5, 163.8, 152.8, 157.7, 157.6, 173.4, 152.2, 176.8, 147.1, 154.3, 
               165.7, 135.5, 55.6, 25.0]

# Convert start times to seconds from the start
seconds_from_start = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) +
                      int(t.split(".")[1]) / 1000) for t in times]

plt.plot(seconds_from_start, total_loads)
plt.title("Total CPU Load % Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Total CPU Load %")

plt.gca().yaxis.grid(True)
plt.show()
