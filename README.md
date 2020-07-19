# Bird Eye View using Stretch Transform

1. Download or clone this repo
2. Navigate to the repo on the hard disk using Anaconda Prompt 
3. Run **python IPM.py**

The screen capture parameters on **Line 47** are:
monitor = {"top": 340, "left": 200, "width": 600, "height": 250}

(If width and height is modified, also change **Line 12** to ensure correct calculation of total pixels in the image)

The resize dimensions in **Line 62** may need to be tuned to obtain a better bird's eye view. This parameter needs to set only once:

capture = cv2.resize(gamma, (740, 580), interpolation= cv2.INTER_AREA)

For now its 740x580.

Interpolation ensures that the aspect ratio is maintained