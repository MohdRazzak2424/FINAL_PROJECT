
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
        cv2.circle(img, (point_x2, point_y2), 13, (255, 0, 0), cv2.FILLED)
        # create a line b/w tips of index finger and thumb
        cv2.line(img, (point_x1, point_y1),
                 (point_x2, point_y2), (255, 0, 0), 3)

        # distance b/w tips using hypotenuse
        length = hypot(point_x2-point_x1, point_y2-point_y1)
        # from numpy we find our length,by converting hand range in terms of volume range ie b/w -63.5 to 0
        vol_xy = np.interp(length, [15, 220], [volMin, volMax])
        volbar_y = np.interp(length, [30, 350], [400, 150])
        volper_int = np.interp(length, [30, 350], [0, 100])

        print(vol_xy, int(length))
        volume.SetMasterVolumeLevel(vol_xy, None)

        # Hand range 30 - 350
        # Volume range -63.5 - 0.0
        # creating volume bar for volume level
        # vid ,initial position ,ending position ,rgb ,thickness
        cv2.rectangle(img, (50, 150), (85, 400), (3, 232, 252), 4)
        cv2.rectangle(img, (50, int(volbar_y)), (85, 400),
                      (11, 252, 3), cv2.FILLED)
        cv2.putText(img, f"MOHD RAZZAK CS50X project ", (10, 60),
                    cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
        cv2.putText(img, f"Volume percentage :- {int(volper_int)}%", (40, 135),
                    cv2.FONT_ITALIC, 1, (14, 47, 235), 3)

        # tell the volume percentage ,location,font of text,length,rgb color,thickness
    # Show the video
    cv2.imshow('CS50X PROJECT VOLUME CONTROL DETECTION BY HUMAN HANDS ', img)
    if cv2.waitKey(1) & 0xff == ord(' '):  # By using spacebar delay will stop
        break

captures.release()  # stop cam
cv2.destroyAllWindows()  # close window
