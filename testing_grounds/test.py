import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'testing_grounds.png')

img_rgb = cv2.imread(r'testing_grounds.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('queen_diamonds.png', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)


threshold = 0.8
loc = np.where(res >= threshold)
with np.printoptions(threshold=np.inf):
    print(loc)
if loc[0].size == 0 or loc[1].size == 0:
    print('yesss???')

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('res.png',img_rgb)