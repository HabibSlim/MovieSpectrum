"""
Defining constants and parameters
"""

# Dimensions of the output spectrum
IMAGE_WIDTH = 1860
IMAGE_HEIGHT = 400

# Number of frame samples to build the spectrum
SAMPLE_NUMBER = 600

# Number of stripes used to detect the movie dimensions
# => TODO : change name
STRIP_NUMBER = 5

# Method used to compute color averages
# 0 => Dumb average
# 1 => Squared average
# 2 => K-Means clustering (costly)
AVG_METHOD = 1
