# cytometry/plots.py

import matplotlib.pyplot as plt

def generate_histogram(data):
    plt.hist(data['channel_name'], bins=20)
    plt.xlabel('Channel Name')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.grid(True)
    return plt.gcf()  # Return the current figure for rendering in template
