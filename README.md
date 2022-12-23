force adding images didnt work
<img width="592" alt="image" src="https://user-images.githubusercontent.com/121255271/209346713-560512b9-81e7-4683-8e07-e3629d965167.png">
 so used stitch method
 




# uasworkaditgupta
started stitching images by creating a stitcher object using open cv
image_paths=["/Users/aditgupta03/Downloads/uas1.jpg","/Users/aditgupta03/Downloads/uas2.jpg","/Users/aditgupta03/Downloads/uas3.jpg","/Users/aditgupta03/Downloads/uas4.jpg","/Users/aditgupta03/Downloads/uas5.jpg"]
#adding image path directorys to a list
imgs = []
#creating a empty list to append and reas images 1 by 1 in a loop
for i in range(len(image_paths)):
    imgs.append(cv2.imread(image_paths[i]))
    #this command helps to append pictures in my empty list
    imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)
  #as pic are large and may be uneven making them even for better stitching
stitchy=cv2.Stitcher.create()
#creating stiching object
(dummy,output)=stitchy.stitch(imgs)
 #for checking and displaying output
if dummy != cv2.STITCHER_OK:
    print("stitching ain't successful")
else:
    print('Your Panorama is ready!!!')

cv2.imshow("final result",output)

cv2.waitkey(0)

images used--![uas1](https://user-images.githubusercontent.com/121255271/209345410-d2aeed61-0e1d-4fe7-ad2d-bb044ae23ca1.jpg)
![uas2](https://user-images.githubusercontent.com/121255271/209345421-7f7733ff-699c-4058-8f67-6c6146178262.jpg)
![uas3](https://user-images.githubusercontent.com/121255271/209345424-0577b05b-27fd-4f46-9a8f-b214435942c8.jpeg)
![uas4](https://user-images.githubusercontent.com/121255271/209345443-09d6c282-5df9-4404-9f4e-312101f64c18.jpg)
![uas5](https://user-images.githubusercontent.com/121255271/209345450-3010d4bd-ca1b-4d49-83b1-2b7bf62a73be.jpg)

final result---
<img width="741" alt="image" src="https://user-images.githubusercontent.com/121255271/209345488-f1175237-c246-4a64-8c7f-9c44be9167ae.png">


some errors--python is case sensitive use for eg. cv2.waitKey and not cv2.waitkey

