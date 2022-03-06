# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import cv2

imp_basic = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Image Cat', imp_basic)
cv2.waitKey(0)
cv2.imwrite('result1.jpg', imp_basic)

cv2.destroyAllWindows()

imp_gray = cv2.cvtColor(imp_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image Gray Cat', imp_gray)
cv2.waitKey(0)
cv2.imwrite('result2.jpg', imp_gray)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
