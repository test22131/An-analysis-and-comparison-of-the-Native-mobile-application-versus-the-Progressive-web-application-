import matplotlib.pyplot as plt

# Data for PWA
times_pwa = [
    "00:00.000.651", "00:01.014.062", "00:02.024.628", "00:03.031.705", "00:04.039.431",
    "00:05.048.038", "00:06.055.945", "00:07.063.584", "00:08.071.127", "00:09.079.660",
    "00:10.087.519", "00:11.096.021", "00:12.101.705", "00:13.109.782", "00:14.113.890",
    "00:15.120.967", "00:16.128.780", "00:17.137.425", "00:18.142.681", "00:19.151.537",
    "00:20.165.822", "00:21.179.722", "00:22.192.746"
]

fps_pwa = [0, 0, 0, 0, 53, 51, 60, 60, 56, 60, 60, 47, 60, 60, 52, 60, 59, 8, 11, 5, 11, 5, 5]

seconds_from_start_pwa = [int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                          int(t.split(".")[1]) / 1000 for t in times_pwa]

# Data for Native Mobile App
times_native = ["00:00.000.000", "00:00.000.513", "00:01.007.747", "00:02.015.515", "00:03.026.902",
         "00:04.034.529", "00:05.041.899", "00:06.049.234", "00:07.052.597", "00:08.059.947",
         "00:09.067.477", "00:10.071.294", "00:11.079.007", "00:12.086.461", "00:13.093.630",
         "00:14.100.644", "00:15.107.448", "00:16.114.483", "00:17.121.281", "00:18.128.143",
         "00:19.134.946", "00:20.141.477", "00:21.148.338", "00:22.155.370"]

fps_native = [0, 8, 8, 8, 8, 8, 8, 10, 43, 40, 38, 41, 48, 45, 24, 44, 31, 53, 38, 44, 29, 12, 8, 8]

seconds_from_start_native = [int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                             int(t.split(".")[1]) / 1000 for t in times_native]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(seconds_from_start_pwa, fps_pwa, color='green', label='PWA')
plt.plot(seconds_from_start_native, fps_native, color='blue', label='Native Mobile App')

plt.title("Frames Per Second Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Frames Per Second (FPS)")
plt.legend(loc='upper left')
plt.gca().yaxis.grid(True)



# Calculate the average FPS for PWA
average_fps_pwa = sum(fps_pwa) / len(fps_pwa)

# Calculate the average FPS for Native Mobile App
average_fps_native = sum(fps_native) / len(fps_native)

# Place the average FPS values as text annotations underneath the x-axis label
x_position = seconds_from_start_pwa[0]  # start of the x-axis
y_position = plt.gca().get_ylim()[0] - 5  # slightly below the graph

plt.text(x_position, y_position, f'PWA Average FPS: {average_fps_pwa:.2f}', color='green', verticalalignment='top')
y_position -= 3  # adjust for the next line
plt.text(x_position, y_position, f'Native Average FPS: {average_fps_native:.2f}', color='blue', verticalalignment='top')

# Adjust the figure to ensure there's enough space at the bottom for the annotations
plt.subplots_adjust(bottom=0.25)

plt.show()




