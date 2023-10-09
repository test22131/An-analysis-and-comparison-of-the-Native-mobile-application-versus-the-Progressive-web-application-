import matplotlib.pyplot as plt

# Raw time data
times = ["00:00.000.000", "00:00.006.542", "00:01.038.829", "00:02.056.125", "00:03.056.570",
         "00:04.057.376", "00:05.058.489", "00:06.058.901", "00:07.109.597", "00:08.158.293",
         "00:09.195.257", "00:10.195.495", "00:11.197.572", "00:12.256.887", "00:13.315.000",
         "00:14.315.294", "00:15.332.778", "00:16.333.209", "00:17.394.641", "00:18.435.313",
         "00:19.452.698", "00:20.486.935", "00:21.490.683", "00:22.547.786"]

# Total Load %
total_loads = [100.0, 49.4, 36.4, 97.4, 118.1, 112.0, 121.4, 127.3, 154.2, 162.0,
               167.4, 158.9, 167.7, 133.8, 120.7, 151.0, 148.0, 171.7, 156.9, 169.2,
               118.3, 45.9, 36.1, 33.6]

# Convert time strings to seconds from the start
seconds_from_start = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                       int(t.split(".")[1]) / 1000) for t in times]

plt.plot(seconds_from_start, total_loads)
plt.title("Total CPU Load % Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Total CPU Load %")

plt.gca().yaxis.grid(True)
plt.show()
