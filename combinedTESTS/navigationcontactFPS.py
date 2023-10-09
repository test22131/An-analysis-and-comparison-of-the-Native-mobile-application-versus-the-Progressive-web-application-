import matplotlib.pyplot as plt

# Data for PWA
times_pwa = [
    "00:00.000.000", "00:00.000.524", "00:01.010.188", "00:02.016.011", "00:03.027.923",
    "00:04.029.924", "00:05.037.641", "00:06.041.420", "00:07.043.213", "00:08.049.855",
    "00:09.056.334", "00:10.062.809", "00:11.069.316", "00:12.071.140", "00:13.077.361",
    "00:14.083.582", "00:15.089.836", "00:16.096.086", "00:17.102.980", "00:18.109.434",
    "00:19.116.747", "00:20.120.419", "00:21.127.195", "00:22.133.772", "00:23.140.252"
]

fps_pwa = [0, 0, 0, 0, 0, 11, 12, 12, 17, 15, 15, 20, 16, 14, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0]

seconds_from_start_pwa = [int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                          int(t.split(".")[1]) / 1000 for t in times_pwa]

# Data for Native Mobile App
times_native = ["00:00.000.000", "00:00.000.391", "00:01.008.299", "00:02.022.400", "00:03.035.794", 
         "00:04.040.984", "00:05.048.732", "00:06.056.766", "00:07.064.728", "00:08.070.448", 
         "00:09.078.899", "00:10.086.987", "00:11.095.633", "00:12.102.826", "00:13.110.844", 
         "00:14.119.410", "00:15.126.870", "00:16.131.175", "00:17.139.451", "00:18.147.148", 
         "00:19.154.945", "00:20.168.485", "00:21.176.431", "00:22.183.660", "00:23.195.521"]

fps_native = [0, 0, 0, 0, 0, 0, 0, 33, 29, 60, 54, 60, 36, 60, 60, 60, 60, 57, 60, 27, 60, 53, 48, 0, 0]

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




