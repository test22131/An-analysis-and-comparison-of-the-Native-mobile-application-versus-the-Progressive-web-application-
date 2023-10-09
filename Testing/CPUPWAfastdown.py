import matplotlib.pyplot as plt

# Raw start time data
times = ["00:01.351.385", "00:02.351.669", "00:03.358.252", "00:04.383.099", "00:05.448.522", 
         "00:06.448.522", "00:07.450.276", "00:08.457.471", "00:09.522.630", "00:10.551.931",
         "00:11.553.710", "00:12.616.082", "00:13.650.526", "00:14.651.416", "00:15.651.965", 
         "00:16.715.711", "00:17.753.714", "00:18.763.160"]

# Total Load %
total_loads = [48.0, 76.5, 98.3, 159.8, 196.3, 204.1, 191.6, 200.6, 201.5, 198.3, 
               202.6, 191.4, 196.1, 196.6, 203.4, 196.2, 130.6, 122.2]

# Convert time strings to seconds from the start
seconds_from_start = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                       int(t.split(".")[1]) / 1000) for t in times]

plt.plot(seconds_from_start, total_loads)
plt.title("Total CPU Load % Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Total Load %")

plt.gca().yaxis.grid(True)
plt.show()
