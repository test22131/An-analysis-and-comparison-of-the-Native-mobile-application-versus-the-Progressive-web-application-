import matplotlib.pyplot as plt

# Raw time data like "32.463.454", "33.463.605", etc., 
# but we are only considering the first two digits before the decimal point.
times = ["32.463.454", "33.463.605", "34.505.950", "35.526.335", "36.593.782",
         "37.656.860", "38.720.805", "39.783.180", "40.846.711", "41.910.239",
         "42.949.074", "43.954.296", "44.954.941", "45.955.934", "47.006.679",
         "48.010.290", "49.073.744", "50.138.493", "51.197.026"]

total_loads = [24.1, 36.5, 57.8, 142.5, 147.5,
               142.2, 137.2, 142.2, 138.7, 130.8,
               141.4, 141.5, 142.4, 135.8, 144.3,
               139.8, 139.6, 108.2, 78.8]

# Convert your time strings to seconds from the start, only considering the first two digits before the decimal point.
seconds_from_start = [int(t.split(".")[0]) for t in times]

plt.plot(seconds_from_start, total_loads)

# Add horizontal grid lines to the plot
plt.gca().yaxis.grid(True)

plt.title("CPU Load Over Time")
plt.xlabel("Time (seconds from start)")
plt.ylabel("CPU Load (%)")
plt.show()
