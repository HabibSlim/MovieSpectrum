import cv2
import numpy as np
import params

from math import sqrt


def frame_offset_column(frame, column):
    """
    Detects special movie formats, like 16:9, and returns offsets in height to adjust for it.

    Args:
        frame: openCV image object
        column: Reading offset in width between 1 et 4

    Returns:
        The offset in height to apply for the n-th (defined by column) strip
    """
    height, width = frame.shape[:2]
    width_cursor = (width // params.STRIP_NUMBER) * column
    top_offset = 0

    for top_shift in range(height):
        pixel_color = frame[top_shift][width_cursor]
        pixel_value = sum(pixel_color)
        if pixel_value:
            top_offset = top_shift
            break

    return top_offset

def frame_offset(frame):
    """
    Detects special movie formats, like 16:9, and returns offsets in height to adjust for it.
    Worker method.

    Args:
        frame: openCV image object
        
    Returns:
        The average offset in height to apply to the frames
    """
    values = [frame_offset_column(frame, n) for n in range(params.STRIP_NUMBER)]
    average_offset = sum(values) // params.STRIP_NUMBER

    height_ceiling = frame.shape[:2][0] // 15

    return average_offset if average_offset > height_ceiling else 0

def dumb_average(frame):
    """
    Returns the average RGB color value from a frame using a simple average

    Args:
        frame: openCV image object
        
    Returns:
        The average RGB color value from a given frame
    """
    avg_color = frame.mean(axis=0).mean(axis=0)

    return list(map(int, avg_color))

def squared_average(frame):
    """
    Returns the average RGB color value from a frame using a simple average

    Args:
        frame: openCV image object
        
    Returns:
        The average RGB color value from a given frame
    """
    squared_frame = np.square(np.array(frame, dtype=np.int32))
    average_color = [int(sqrt(squared_frame[:, :, n].mean())) for n in range(3)]

    return average_color

def dominant_color(frame):
    """
    Returns the dominant RGB color value from a frame using K-Means clustering

    Args:
        frame: openCV image object
        
    Returns:
        The dominant RGB color value from a given frame
    """
    pixels = np.float32(frame.reshape(-1, 3))

    n_colors = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)

    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    _, counts = np.unique(labels, return_counts=True)

    dominant = palette[np.argmax(counts)]

    return list(map(int, dominant))