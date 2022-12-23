import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
image_paths=["/Users/aditgupta03/Downloads/uas1.jpg","/Users/aditgupta03/Downloads/uas2.jpg","/Users/aditgupta03/Downloads/uas3.jpg","/Users/aditgupta03/Downloads/uas4.jpg","/Users/aditgupta03/Downloads/uas5.jpg"]
imgs = []
 
for i in range(len(image_paths)):
    imgs.append(cv2.imread(image_paths[i]))
    imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)

stitchy=cv2.Stitcher.create()
(dummy,output)=stitchy.stitch(imgs)
 
if dummy != cv2.STITCHER_OK:
    print("stitching ain't successful")
else:
    print('Your Panorama is ready!!!')

cv2.imshow("final result",output)

cv2.waitkey(0)
