import matplotlib.pyplot as plt

# PWA data
pwa_times = ["00:01.011.234", "00:02.024.251", "00:03.067.971", "00:04.073.837", "00:05.137.066",
         "00:06.171.755", "00:07.171.331", "00:08.172.161", "00:09.173.135", "00:10.207.343", 
         "00:11.266.486", "00:12.309.710", "00:13.312.805", "00:14.317.324", "00:15.345.155", 
         "00:16.351.247", "00:17.388.320", "00:18.409.315", "00:19.409.692", "00:20.417.184", 
         "00:21.418.400", "00:22.421.355"]
pwa_loads = [48.5, 102.2, 119.5, 162.5, 151.2, 154.7, 152.4, 172.3, 143.5, 158.0,
               164.8, 218.9, 173.1, 117.9, 117.4, 122.6, 118.1, 117.7, 121.5, 120.8, 
               116.3, 121.7]

# Native mobile application data
native_times = ["00:00.000.000", "00:00.341.968", "00:01.342.690", "00:02.403.346", "00:03.439.155", 
         "00:04.440.197", "00:05.471.649", "00:06.474.324", "00:07.538.207", "00:08.600.443", 
         "00:09.601.966", "00:10.646.900", "00:11.675.766", "00:12.684.693", "00:13.690.113", 
         "00:14.730.346", "00:15.747.747", "00:16.761.404", "00:17.787.661", "00:18.808.236", 
         "00:19.840.444", "00:20.843.532", "00:21.878.676", "00:22.941.463"]
native_loads = [50, 61.9, 118.7, 72.7, 168.6, 118.9, 118.1, 164.2, 144.3, 179.6, 
               153.5, 163.8, 152.8, 157.7, 157.6, 173.4, 152.2, 176.8, 147.1, 154.3, 
               165.7, 135.5, 55.6, 25.0]

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
