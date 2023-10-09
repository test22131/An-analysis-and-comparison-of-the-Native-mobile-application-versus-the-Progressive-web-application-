import matplotlib.pyplot as plt

# PWA data
pwa_times = ["00:00.008.170","00:01.012.371","00:02.012.965","00:03.037.550","00:04.047.192","00:05.079.773","00:06.151.243","00:07.155.004","00:08.182.422","00:09.184.186","00:10.184.147","00:11.189.990","00:12.196.773","00:13.256.334","00:14.256.364","00:15.282.258","00:16.342.105","00:17.348.065","00:18.377.119","00:19.378.773","00:20.429.747","00:21.463.180","00:22.481.288"]

pwa_loads = [50.1, 36.8, 91.8, 111.8, 181.2, 160.7, 166.0, 189.0, 176.6, 172.8, 171.7, 
              156.4, 170.1, 182.2, 155.4, 174.8, 155.5, 127.4, 116.7, 50.7, 45.5, 48.0, 27.6]

# Native mobile application data
native_times = ["00:00.000.000", "00:00.006.542", "00:01.038.829", "00:02.056.125", "00:03.056.570",
         "00:04.057.376", "00:05.058.489", "00:06.058.901", "00:07.109.597", "00:08.158.293",
         "00:09.195.257", "00:10.195.495", "00:11.197.572", "00:12.256.887", "00:13.315.000",
         "00:14.315.294", "00:15.332.778", "00:16.333.209", "00:17.394.641", "00:18.435.313",
         "00:19.452.698", "00:20.486.935", "00:21.490.683", "00:22.547.786"]
native_loads = [100.0, 49.4, 36.4, 97.4, 118.1, 112.0, 121.4, 127.3, 154.2, 162.0,
               167.4, 158.9, 167.7, 133.8, 120.7, 151.0, 148.0, 171.7, 156.9, 169.2,
               118.3, 45.9, 36.1, 33.6]

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
y_position = plt.gca().get_ylim()[0] - 15  # slightly below the graph

plt.text(x_position, y_position, f'PWA Average Load: {average_load_pwa:.2f}%', color='green', verticalalignment='top')
y_position -= 7  # adjust for the next line
plt.text(x_position, y_position, f'Native Average Load: {average_load_native:.2f}%', color='blue', verticalalignment='top')

# Adjust the figure to ensure there's enough space at the bottom for the annotations
plt.subplots_adjust(bottom=0.25)

plt.show()
