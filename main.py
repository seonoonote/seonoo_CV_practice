# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import cv2

img_basic = cv2.imread('cat.jpg')
cv2.imshow('Image Cat', img_basic)
cv2.waitKey(0)
cv2.imwrite('result1.jpg', img_basic)

cv2.destroyAllWindows()

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image Gray Cat', img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.jpg', img_gray)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
