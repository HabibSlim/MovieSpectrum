#!/usr/bin/env python3

import cv2
import numpy as np
import params
import sys

from framemath import *

def compute_average(frame):
    avg_functions = [dumb_average, squared_average, dominant_color]
    avg_color = avg_functions[params.AVG_METHOD](frame)

    return avg_color

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Usage : ./spectrum.py path_to_video_file")
        exit()

    capture = cv2.VideoCapture(path)
    spectrum = np.zeros((params.IMAGE_HEIGHT, params.IMAGE_WIDTH, 3), np.uint8)

    # Working out video indexes
    maxFrames = capture.get(7)
    frameindex = maxFrames // 2
    framestep = maxFrames // params.SAMPLE_NUMBER

    stripe_width = params.IMAGE_WIDTH // params.SAMPLE_NUMBER
    stripe_x_pos = 0

    # Guessing the video dimension from the middle frame
    capture.set(1, frameindex)
    ret, frame = capture.read()
    height_crop = frame_offset(frame)

    frameindex = 0
    capture.set(1, frameindex)

    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret:
            # Cropping the frame to adjust for movie formats
            if height_crop:
                frame = frame[height_crop:-height_crop]

            avg_color = compute_average(frame)
            print(avg_color)
            frame[:] = avg_color

            # Adding the average color to the output spectrum
            spectrum[:,stripe_x_pos:stripe_x_pos+stripe_width] = avg_color
            stripe_x_pos += stripe_width 

            cv2.imshow('MovieSpectrum', spectrum)
            cv2.waitKey(1)

            frameindex += framestep
            capture.set(1, frameindex)
        else:
            break

    while True:
        char = cv2.waitKey(50)
        if 'q' == chr(char & 255):
            cv2.destroyAllWindows()
            break
    
if (__name__ == "__main__"):
    main()