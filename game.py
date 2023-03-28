import cv2 as cv
import cv2
import numpy as np
import os
import time
from windowcapture import WindowCapture
import pyautogui

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def pressSpaceButton():
    time.sleep(0.15)
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')

def match(haystack_img, needle_img, threshold, name):

    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_SQDIFF_NORMED)

# I've inverted the threshold and where comparison to work with TM_SQDIFF_NORMED
    # threshold = threshold
# The np.where() return value will look like this:
# (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
    locations = np.where(result <= threshold)
# We can zip those up into a list of (x, y) position tuples
    locations = list(zip(*locations[::-1]))
    print(locations)
    print(len(locations))
    # time.sleep(10)

    if locations:
        print('Found needle.')

        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

    # Loop over all the locations and draw their rectangle
        for loc in locations:
        # Determine the box positions
            top_left = loc
            bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
            # print(top_left)
            # print(bottom_right)
        # Draw the box
            cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)

        # print(top_left, bottom_right)
        # time.sleep(20)
        text = "{}".format(name)
        cv.putText(haystack_img, text, top_left, cv.FONT_HERSHEY_COMPLEX, color=(255,0,0), fontScale=1.2)
        return haystack_img
    #cv.imwrite('result.jpg', haystack_img)

    else:
        return haystack_img        


# initialize the WindowCapture class
wincap = WindowCapture('黑色跳跳球')

needle_img = cv.imread('ball.png', cv.IMREAD_COLOR)
star_img = cv.imread('star.png', cv.IMREAD_COLOR)
final_img = cv.imread('final.png', cv.IMREAD_COLOR)

loop_time = time.time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    img = match(screenshot, needle_img, 0.3, name='ball')
    img = match(img, star_img, 0.05, name='star')
    img = match(img, final_img, 0.1, name='final')

    # img = match(screenshot, needle_img)
    cv.imshow('Computer Vision', img)
    #pressSpaceButton()
    # debug the loop rate
    print('FPS {}'.format(1 / (time.time() - loop_time)))
    loop_time = time.time()
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
