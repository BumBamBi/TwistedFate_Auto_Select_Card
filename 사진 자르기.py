import sys
import cv2
from time import sleep

a = cv2.imread('image/card.png')

b = a[0:360, 238:453]   #215
cv2.imshow('aa', b)
cv2.imwrite('testt.png', b)
cv2.waitKey(0)
cv2.destroyAllWindows()