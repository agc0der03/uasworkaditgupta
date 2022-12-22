import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

im_g = cv.imread("/Users/aditgupta03/Downloads/watch.jpg")

#cv.imshow("image",im_g)
#cv.waitKey(0)
#cv.destroyAllWindows()
plt.imshow(im_g,cmap="Blues",interpolation="bicubic")
plt.show()

