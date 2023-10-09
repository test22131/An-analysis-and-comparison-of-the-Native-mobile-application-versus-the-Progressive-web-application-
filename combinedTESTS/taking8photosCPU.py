import matplotlib.pyplot as plt

# PWA data
pwa_times = [
    "00:00.000.000", "00:00.014.021", "00:01.016.668", "00:02.044.731", "00:03.052.212",
    "00:04.078.743", "00:05.079.653", "00:06.143.474", "00:07.181.383", "00:08.181.955",
    "00:09.187.383", "00:10.251.405", "00:11.276.354", "00:12.277.387", "00:13.311.202",
    "00:14.313.591", "00:15.317.463", "00:16.326.943", "00:17.330.612", "00:18.337.531",
    "00:19.382.330", "00:20.384.689", "00:21.450.697", "00:22.484.531", "00:23.545.857",
    "00:24.553.316", "00:25.554.225"
]
pwa_loads = [0.0, 120.0, 83.7, 116.0, 180.3, 187.3, 190.6, 192.0, 173.5, 183.2, 197.6, 209.2, 165.9, 
              190.8, 166.6, 180.7, 179.1, 194.4, 181.8, 199.7, 161.4, 171.6, 171.4, 152.8, 172.7, 148.6, 156.8]

# Native mobile application data
native_times = [
    "00:00.000.000", "00:00.346.826", "00:01.348.287", "00:02.360.790", "00:03.415.717",
    "00:04.418.162", "00:05.450.549", "00:06.463.773", "00:07.465.166", "00:08.500.535",
    "00:09.502.159", "00:10.509.961", "00:11.567.708", "00:12.619.040", "00:13.669.517",
    "00:14.671.043", "00:15.671.260", "00:16.672.021", "00:17.674.975", "00:18.677.220",
    "00:19.694.956", "00:20.700.387", "00:21.708.791", "00:22.711.024", "00:23.712.251",
    "00:24.711.875", "00:25.712.822", "00:26.714.739"
]
native_loads = [0.0, 42.0, 34.7, 75.8, 156.3, 227.8, 198.8, 204.0, 215.6, 206.0, 199.3, 237.1, 202.9, 
              201.8, 188.5, 230.8, 190.0, 184.0, 232.1, 204.4, 200.0, 224.2, 180.7, 134.1, 177.3, 167.6, 143.5, 163.7]

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
y_position = plt.gca().get_ylim()[0] - 17  # slightly below the graph

plt.text(x_position, y_position, f'PWA Average Load: {average_load_pwa:.2f}%', color='green', verticalalignment='top')
y_position -= 8  # adjust for the next line
plt.text(x_position, y_position, f'Native Average Load: {average_load_native:.2f}%', color='blue', verticalalignment='top')

# Adjust the figure to ensure there's enough space at the bottom for the annotations
plt.subplots_adjust(bottom=0.25)

plt.show()
