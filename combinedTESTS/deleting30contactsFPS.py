import matplotlib.pyplot as plt

# Data for PWA
times_pwa = [
    "00:02.028.388", "00:03.042.053", "00:04.050.455", "00:05.056.204",
    "00:06.063.454", "00:07.067.980", "00:08.073.446", "00:09.080.095",
    "00:10.088.026", "00:11.098.587", "00:12.108.062", "00:13.117.290",
    "00:14.125.168", "00:15.134.042", "00:16.142.557", "00:17.149.181",
    "00:18.153.747", "00:19.161.751", "00:20.169.266", "00:21.177.029"
]

fps_pwa = [3, 3, 4, 17, 10, 13, 15, 12, 10, 13, 11, 9, 13, 11, 17, 6, 14, 13, 25, 5]

seconds_from_start_pwa = [int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                          int(t.split(".")[1]) / 1000 for t in times_pwa]

# Data for Native Mobile App
times_native = ["00:02.026.158", "00:03.040.326", "00:04.048.750", "00:05.057.137", "00:06.061.572", 
             "00:07.069.926", "00:08.077.067", "00:09.084.999", "00:10.091.807", "00:11.099.645", 
             "00:12.107.942", "00:13.117.661", "00:14.121.904", "00:15.127.336", "00:16.137.645", 
             "00:17.144.160", "00:18.153.756", "00:19.162.551", "00:20.171.319"]

fps_native = [0, 0, 0, 6, 21, 22, 24, 25, 23, 26, 20, 18, 22, 26, 19, 21, 25, 0, 0]

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
y_position = plt.gca().get_ylim()[0] - 3  # slightly below the graph

plt.text(x_position, y_position, f'PWA Average FPS: {average_fps_pwa:.2f}', color='green', verticalalignment='top')
y_position -= 1  # adjust for the next line
plt.text(x_position, y_position, f'Native Average FPS: {average_fps_native:.2f}', color='blue', verticalalignment='top')

# Adjust the figure to ensure there's enough space at the bottom for the annotations
plt.subplots_adjust(bottom=0.25)

plt.show()




