import cv2
import time
import mss
import numpy as np

def gamma_correction_auto(RGBimage, equalizeHist = False):
    originalFile = RGBimage.copy()
    red = RGBimage[:,:,2]
    green = RGBimage[:,:,1]
    blue = RGBimage[:,:,0]

    vidsize = (600, 250)
    forLuminance = cv2.cvtColor(originalFile,cv2.COLOR_BGR2YUV)
    Y = forLuminance[:,:,0]
    totalPix = vidsize[0]* vidsize[1]
    summ = np.sum(Y[:,:])
    Yaverage = np.divide(totalPix,summ)

    epsilon = 1.19209e-007
    correct_param = np.divide(-0.3,np.log10([Yaverage + epsilon]))
    correct_param = 0.7 - correct_param 

    red = red/255.0
    red = cv2.pow(red, correct_param)
    red = np.uint8(red*255)
    if equalizeHist:
        red = cv2.equalizeHist(red)
    
    green = green/255.0
    green = cv2.pow(green, correct_param)
    green = np.uint8(green*255)
    if equalizeHist:
        green = cv2.equalizeHist(green)
        
    blue = blue/255.0
    blue = cv2.pow(blue, correct_param)
    blue = np.uint8(blue*255)
    if equalizeHist:
        blue = cv2.equalizeHist(blue)
    
    output = cv2.merge((blue,green,red))
    #print(correct_param)
    return output

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 340, "left": 200, "width": 600, "height": 250}

    #monitor = {"top": 340, "left": 200, "width": 520, "height": 100}
    

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        screen = np.array(sct.grab(monitor))
        screen = np.flip(screen[:, :, :3], 2)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

        gamma = gamma_correction_auto(screen, equalizeHist = False)

        capture = cv2.resize(gamma, (740, 580), interpolation= cv2.INTER_AREA)

        #capture = cv2.resize(gamma, (640, 480), interpolation= cv2.INTER_AREA)

        print("fps: {}".format(1 / (time.time() - last_time)))

        cv2.imshow('Screen Capture', gamma)
        cv2.imshow('Resized', capture)

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
