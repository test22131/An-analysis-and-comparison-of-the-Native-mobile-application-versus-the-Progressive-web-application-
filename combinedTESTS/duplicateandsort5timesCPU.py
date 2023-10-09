import matplotlib.pyplot as plt

# PWA data
pwa_times = ["00:00.000.000", "00:00.006.911", "00:01.011.546", "00:02.049.739", "00:03.080.991",
         "00:04.087.487", "00:05.101.656", "00:06.102.533", "00:07.124.511", "00:08.177.166",
         "00:09.189.737", "00:10.196.700", "00:11.205.160", "00:12.221.681", "00:13.230.228",
         "00:14.230.370", "00:15.244.995", "00:16.282.715", "00:17.296.662", "00:18.300.945",
         "00:19.301.739"]
pwa_loads = [0.0, 42.8, 33.8, 87.0, 111.3, 221.0, 217.6, 216.7, 210.3, 146.6, 
              173.0, 122.7, 120.4, 114.3, 115.4, 112.2, 111.2, 112.8, 114.0, 113.7, 116.5]

# Native mobile application data
native_times = ["00:00.000.000", "00:00.007.555", "00:01.011.698", "00:02.071.752", "00:03.124.795", 
         "00:04.132.711", "00:05.141.686", "00:06.144.654", "00:07.159.330", "00:08.173.127",
         "00:09.173.557", "00:10.181.286", "00:11.192.510", "00:12.236.999", "00:13.263.957",
         "00:14.271.232", "00:15.318.230", "00:16.350.390", "00:17.395.231", "00:18.403.037",
         "00:19.446.563", "00:20.464.527"]
native_loads = [100.0, 42.8, 42.5, 80.6, 160.6, 161.7, 110.6, 124.9, 168.0, 183.5, 200.4, 178.9, 215.4, 189.5, 125.7, 116.4, 118.9, 116.9, 111.8, 113.8, 119.3, 112.0]

# Convert time strings to seconds from the start for both data sets
pwa_seconds = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + int(t.split(".")[1]) / 1000) for t in pwa_times]
native_seconds = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + int(t.split(".")[1]) / 1000) for t in native_times]

# Plotting the data
plt.plot(pwa_seconds, pwa_loads, color='green', label='PWA')
plt.plot(native_seconds, native_loads, color='blue', label='Native Mobile App')

# Setting graph attributes
plt.title("Total CPU Load % Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Total CPU Load %")
plt.legend(loc='upper left')  # Display the legend
plt.gca().yaxis.grid(True)

# Calculate the average CPU Load for PWA
average_load_pwa = sum(pwa_loads) / len(pwa_loads)

# Calculate the average CPU Load for Native Mobile App
average_load_native = sum(native_loads) / len(native_loads)

# Place the average Load values as text annotations underneath the x-axis label
x_position = pwa_seconds[0]  # start of the x-axis
y_position = plt.gca().get_ylim()[0] - 19  # slightly below the graph

plt.text(x_position, y_position, f'PWA Average Load: {average_load_pwa:.2f}%', color='green', verticalalignment='top')
y_position -= 8  # adjust for the next line
plt.text(x_position, y_position, f'Native Average Load: {average_load_native:.2f}%', color='blue', verticalalignment='top')

# Adjust the figure to ensure there's enough space at the bottom for the annotations
plt.subplots_adjust(bottom=0.25)

plt.show()
