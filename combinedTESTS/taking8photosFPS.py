import matplotlib.pyplot as plt

# Data for PWA
times_pwa = [
    "00:00.000.000", "00:00.000.609", "00:01.013.651", "00:02.022.111", "00:03.031.602",
    "00:04.035.945", "00:05.041.411", "00:06.049.633", "00:07.052.822", "00:08.060.225",
    "00:09.068.129", "00:10.073.192", "00:11.077.878", "00:12.085.813", "00:13.093.750",
    "00:14.103.260", "00:15.111.315", "00:16.119.789", "00:17.128.129", "00:18.133.545",
    "00:19.139.893", "00:20.146.538", "00:21.152.202"
]

fps_pwa = [0, 0, 0, 0, 13, 40, 60, 60, 32, 32, 34, 33, 32, 32, 55, 51, 33, 32, 13, 27, 41, 59, 56]

seconds_from_start_pwa = [int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                          int(t.split(".")[1]) / 1000 for t in times_pwa]

# Data for Native Mobile App
times_native = [
    "00:00.000.000", "00:00.000.486", "00:01.012.112", "00:02.022.873", "00:03.036.501",
    "00:04.045.920", "00:05.054.659", "00:06.058.740", "00:07.067.082", "00:08.078.492",
    "00:09.086.223", "00:10.095.342", "00:11.102.658", "00:12.112.534", "00:13.121.459",
    "00:14.128.185", "00:15.136.115", "00:16.143.908", "00:17.152.283", "00:18.160.809",
    "00:19.167.154", "00:20.175.032", "00:21.182.988", "00:22.189.813", "00:23.197.686",
    "00:24.205.726", "00:25.215.162", "00:26.227.128"
]

fps_native = [0, 0, 0, 0, 27, 60, 60, 60, 60, 60, 60, 60, 60, 59, 59, 60, 60, 60, 60, 60, 59, 60, 60, 59, 60, 60, 60, 60]

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




