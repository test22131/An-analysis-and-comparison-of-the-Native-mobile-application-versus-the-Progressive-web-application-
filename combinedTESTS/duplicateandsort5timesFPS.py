import matplotlib.pyplot as plt

# Data for PWA
times_pwa = ["00:00.000.000", "00:00.000.579", "00:01.011.545", "00:02.025.634", "00:03.037.078",
         "00:04.044.361", "00:05.050.852", "00:06.055.588", "00:07.062.952", "00:08.069.141",
         "00:09.075.299", "00:10.082.093", "00:11.088.981", "00:12.095.772", "00:13.102.390",
         "00:14.108.937", "00:15.115.612", "00:16.122.534", "00:17.129.240", "00:18.135.668",
         "00:19.142.135"]

fps_pwa = [0, 0, 0, 0, 6, 6, 12, 6, 6, 1, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

seconds_from_start_pwa = [int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                          int(t.split(".")[1]) / 1000 for t in times_pwa]

# Data for Native Mobile App
times_native = ["00:00.000.000", "00:00.000.955", "00:01.012.718", "00:02.024.354", "00:03.030.981", 
         "00:04.039.308", "00:05.048.614", "00:06.056.257", "00:07.064.356", "00:08.072.106",
         "00:09.079.783", "00:10.084.196", "00:11.092.242", "00:12.097.105", "00:13.102.535",
         "00:14.111.317", "00:15.116.565", "00:16.127.722", "00:17.136.868", "00:18.145.869",
         "00:19.154.572", "00:20.163.826"]

fps_native = [0, 0, 0, 0, 0, 32, 6, 1, 29, 17, 3, 0, 0, 0, 29, 0, 0, 0, 0, 0, 0, 0]

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
y_position = plt.gca().get_ylim()[0] - 4  # slightly below the graph

plt.text(x_position, y_position, f'PWA Average FPS: {average_fps_pwa:.2f}', color='green', verticalalignment='top')
y_position -= 2  # adjust for the next line
plt.text(x_position, y_position, f'Native Average FPS: {average_fps_native:.2f}', color='blue', verticalalignment='top')

# Adjust the figure to ensure there's enough space at the bottom for the annotations
plt.subplots_adjust(bottom=0.25)

plt.show()




