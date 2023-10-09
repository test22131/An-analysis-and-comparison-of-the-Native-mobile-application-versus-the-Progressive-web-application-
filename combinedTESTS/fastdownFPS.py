import matplotlib.pyplot as plt

# Data for PWA
times_pwa = ["00:00.000.000", "00:00.000.602", "00:01.013.571", "00:02.022.805", "00:03.031.592", 
             "00:04.037.876", "00:05.045.797", "00:06.053.493", "00:07.061.179", "00:08.068.907",
             "00:09.077.247", "00:10.081.751", "00:11.087.242", "00:12.097.021", "00:13.105.311", 
             "00:14.112.826", "00:15.118.221", "00:16.122.033", "00:17.131.132", "00:18.140.167",
             "00:19.145.385", "00:20.154.175"]

fps_pwa = [0, 0, 0, 0, 0, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 29, 30, 14]

seconds_from_start_pwa = [int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                          int(t.split(".")[1]) / 1000 for t in times_pwa]

# Data for Native Mobile App
times_native = ["00:00.000.000", "00:00.000.575", "00:01.010.997", "00:02.023.555", "00:03.030.969", 
                "00:04.038.106", "00:05.043.060", "00:06.050.029", "00:07.056.836", "00:08.062.023", 
                "00:09.069.523", "00:10.075.722", "00:11.083.631", "00:12.091.542", "00:13.095.072", 
                "00:14.098.532", "00:15.105.969", "00:16.113.398", "00:17.117.822", "00:18.125.524"]

fps_native = [0, 0, 0, 0, 0, 23, 60, 60, 60, 60, 55, 60, 60, 60, 60, 60, 14, 4, 0, 0]

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
y_position = plt.gca().get_ylim()[0] - 8  # slightly below the graph

plt.text(x_position, y_position, f'PWA Average FPS: {average_fps_pwa:.2f}', color='green', verticalalignment='top')
y_position -= 3  # adjust for the next line
plt.text(x_position, y_position, f'Native Average FPS: {average_fps_native:.2f}', color='blue', verticalalignment='top')

# Adjust the figure to ensure there's enough space at the bottom for the annotations
plt.subplots_adjust(bottom=0.25)

plt.show()




