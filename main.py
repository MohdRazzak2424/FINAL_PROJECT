from colorsys import rgb_to_hls, rgb_to_hsv, rgb_to_yiq
from ctypes import POINTER, cast
from ctypes.wintypes import RGB
from math import hypot

import cv2
import mediapipe as mp
import numpy as np
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

captures = cv2.VideoCapture(0)  # Checks for camera

my_mpHands = mp.solutions.hands  # detects hand/finger
hands = my_mpHands.Hands()  # complete the initialization configuration of hands
mpDraw = mp.solutions.drawing_utils

# To access speaker through the library pycaw
devices = AudioUtilities.GetSpeakers()
my_interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(my_interface, POINTER(IAudioEndpointVolume))
volume_bar = 400
volume_percentage = 0

volMin, volMax = volume.GetVolumeRange()[:2]  # type: ignore

while True:
    achieved, img = captures.read()  # If camera works capture an image
    my_imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to rgb

    # Collection of gesture information
    # completes the image processing.
    results_obtained = hands.process(my_imgRGB)

    my_lmList = []  # empty list
    if results_obtained.multi_hand_landmarks:  # list of all hands detected.
        # By accessing the list, we can get the information of each hand's corresponding flag bit
        for handlandmark in results_obtained.multi_hand_landmarks:
            # adding counter and returning it
            for id, lm in enumerate(handlandmark.landmark):
                # Get finger joint points
                h, w, _ = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # adding to the empty list 'lmList'
                my_lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(
                img, handlandmark, my_mpHands.HAND_CONNECTIONS)

    if my_lmList != []:
        # getting the value at a point
        # x      #y
        point_x1, point_y1 = my_lmList[4][1], my_lmList[4][2]  # thumb
        point_x2, point_y2 = my_lmList[8][1], my_lmList[8][2]  # index finger
        # creating circle at the tips of thumb and index finger
        # image #fingers #radius #rgb
        cv2.circle(img, (point_x1, point_x1), 13, (255, 0, 0), cv2.FILLED)
        # image #fingers #radius #rgb
              
