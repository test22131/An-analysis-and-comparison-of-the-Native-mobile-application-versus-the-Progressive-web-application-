import matplotlib.pyplot as plt

# PWA data
pwa_times = ["00:01.351.385", "00:02.351.669", "00:03.358.252", "00:04.383.099", "00:05.448.522", 
             "00:06.448.522", "00:07.450.276", "00:08.457.471", "00:09.522.630", "00:10.551.931",
             "00:11.553.710", "00:12.616.082", "00:13.650.526", "00:14.651.416", "00:15.651.965", 
             "00:16.715.711", "00:17.753.714", "00:18.763.160"]
pwa_loads = [48.0, 76.5, 98.3, 159.8, 196.3, 204.1, 191.6, 200.6, 201.5, 198.3, 202.6, 191.4, 196.1, 196.6, 203.4, 196.2, 130.6, 122.2]

# Native mobile application data
native_times = ["00:00.000.000", "00:00.343.042", "00:01.346.938", "00:02.366.147", "00:03.374.059", 
                "00:04.426.318", "00:05.483.760", "00:06.510.705", "00:07.511.347", "00:08.512.889", 
                "00:09.573.267", "00:10.608.912", "00:11.674.062", "00:12.707.047", "00:13.711.644", 
                "00:14.745.401", "00:15.747.786", "00:16.788.337", "00:17.815.357"]
native_loads = [25, 47.7, 28.4, 74.6, 113.9, 124.5, 184.7, 190.4, 183.4, 189.4, 189.4, 185.8, 195.4, 194.8, 181.8, 158.8, 114.2, 177.2, 115.1]

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
