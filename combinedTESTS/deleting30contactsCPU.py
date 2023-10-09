import matplotlib.pyplot as plt

# PWA data
pwa_times = [
    "00:00.000.000", "00:00.344.403", "00:01.348.250", "00:02.412.555", "00:03.448.106", 
    "00:04.456.418", "00:05.491.325", "00:06.491.304", "00:07.491.838", "00:08.548.697", 
    "00:09.550.590", "00:10.578.750", "00:11.588.426", "00:12.646.294", "00:13.697.166", 
    "00:14.699.981", "00:15.749.271", "00:16.749.692", "00:17.766.556", "00:18.818.552", 
    "00:19.831.595", "00:20.834.930", "00:21.840.088"
]
pwa_loads = [0.0, 103.4, 97.5, 88.0, 136.0, 175.5, 178.9, 177.7, 156.6, 185.1, 171.2,
    181.4, 174.2, 160.5, 186.6, 180.3, 167.5, 188.8, 173.4, 174.8, 175.5, 159.7, 125.2]

# Native mobile application data
native_times = ["00:00.000.000", "00:00.339.467", "00:01.344.588", "00:02.365.670", "00:03.413.670", 
               "00:04.417.476", "00:05.476.237", "00:06.509.525", "00:07.509.504", "00:08.510.225",
               "00:09.516.458", "00:10.544.127", "00:11.544.188", "00:12.544.722", "00:13.544.851", 
               "00:14.549.487", "00:15.599.691", "00:16.647.975", "00:17.652.326", "00:18.662.997", 
               "00:19.667.818"]
native_loads = [0.0, 35.7, 36.3, 72.8, 114.6, 124.3, 170.9, 188.0, 177.5, 171.4, 
               176.9, 173.6, 180.9, 173.4, 181.3, 178.9, 175.8, 181.5, 181.6, 
               116.6, 115.4]

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
