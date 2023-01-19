# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import pyrealsense2 as rs
import matplotlib.pyplot as plt
import numpy as np
import cv2
# Press the green button in the gutter to run the script.


import scipy.io


def main():

    pipeline_1 = rs.pipeline()
    config_1 = rs.config()
    # config_1.enable_device('802212060621')
    config_1.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    # config_1.enable_stream(rs.stream.depth, 640, 480, rs.format.bgr8, 30)
    config_1.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

    # Start streaming from both cameras
    pipeline_1.start(config_1)
    img_counter = 0
    # try:
    while True:
        # Camera 1
        # Wait for a coherent pair of frames: depth and color
        frames_1 = pipeline_1.wait_for_frames()
        depth_frame_1 = frames_1.get_depth_frame()
        color_frame_1 = frames_1.get_color_frame()
        # color_frame_1 = frames_1.get_color_frame()
        # if not depth_frame_1:
        #     continue
        depth_image_1 = np.asanyarray(depth_frame_1.get_data())
        color_image_1 = np.asanyarray(color_frame_1.get_data())

        depth_colormap_1 = cv2.applyColorMap(cv2.convertScaleAbs(depth_image_1, alpha=0.5), cv2.COLORMAP_JET)
        cv2.namedWindow('RealSense', cv2.WINDOW_NORMAL)
        cv2.imshow('RealSense', depth_colormap_1)
        cv2.waitKey(1)
        # plt.imshow(color_image_1)
        # plt.show()
        import time
        # time.sleep(1000)
    # except Exception as e:
    #     print(e)
    #     pass
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
