import FlowCal
import matplotlib.pyplot as plt
# Load FCS data
data = FlowCal.io.FCSData('1.fcs')
# Plot histograms for all channels
FlowCal.plot.hist1d(data, channel='FL1-H')
plt.show()

# Plot a scatter plot
FlowCal.plot.scatter2d(data, channels=('FL1-H', 'FL2-H'))
plt.show()

FlowCal.plot.hist1d(data, channel='FL1-H', alpha=0.7, bins=128)
FlowCal.plot.hist1d(data, channel='FL2-H', alpha=0.7, bins=128)
plt.show()

# Plot density plot
plt.figure(figsize=(8, 6))
FlowCal.plot.density2d(data, channels=['FL1-H', 'FL2-H'])
plt.xlabel('FSC')
plt.ylabel('SSC')
plt.title('2D Density Plot')
plt.show()

# Extract time data (assuming your FCS file has a time channel named 'Time')
time_data = data[:, 'Time']

# Plot time series plot
plt.figure(figsize=(8, 6))
plt.plot(time_data, fluorescence_data, marker='o', linestyle='-')
plt.xlabel('Time')
plt.ylabel('Fluorescence Intensity')
plt.title('Fluorescence Intensity Over Time')
plt.show()
