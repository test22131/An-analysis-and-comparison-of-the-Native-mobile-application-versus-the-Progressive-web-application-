import matplotlib.pyplot as plt

# Raw start time data
times = ["00:00.000.000", "00:00.339.467", "00:01.344.588", "00:02.365.670", "00:03.413.670", 
               "00:04.417.476", "00:05.476.237", "00:06.509.525", "00:07.509.504", "00:08.510.225",
               "00:09.516.458", "00:10.544.127", "00:11.544.188", "00:12.544.722", "00:13.544.851", 
               "00:14.549.487", "00:15.599.691", "00:16.647.975", "00:17.652.326", "00:18.662.997", 
               "00:19.667.818"]

# Total Load %
total_loads = [0.0, 35.7, 36.3, 72.8, 114.6, 124.3, 170.9, 188.0, 177.5, 171.4, 
               176.9, 173.6, 180.9, 173.4, 181.3, 178.9, 175.8, 181.5, 181.6, 
               116.6, 115.4]

# Convert time strings to seconds from the start
seconds_from_start = [(int(t.split(":")[0])*60 + int(t.split(":")[1].split(".")[0]) + 
                       int(t.split(".")[1]) / 1000) for t in times]

plt.plot(seconds_from_start, total_loads)
plt.title("Total Load % Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("Total Load %")

plt.gca().yaxis.grid(True)
plt.show()
