#READING DAY 1 IMAGE
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage.color import rgb2lab, deltaE_cie76
path=r'C:\Users\nvnmu\Desktop\day1.jpg'
img2=cv2.imread(path)
img1 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
plt.imshow(img1)


# CHECKING GREEN CONTENT AND RED CONTENT IN THE LEAF ON DAY 1
day_n_g, day_n_r, day_n_b = 0, 0, 0
for i in range(len(img1)):
    for j in range(len(img1[1])):
        day_n_r+=img1[i][j][0]
        day_n_g+=img1[i][j][1]
        day_n_b+=img1[i][j][2]
print("day n  red is: ", day_n_r, "  day n green is: ", day_n_g, " day n  blue is :  ", day_n_b)


# READING DAY 3 IMAGE
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
path=r'C:\Users\nvnmu\Desktop\day3.jpg'
img2=cv2.imread(path)
img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
plt.imshow(img3)

# CHECKING GREEN CONTENT AND RED CONTENT IN THE LEAF ON DAY 3
day_n2_g, day_n2_r, day_n2_b = 0, 0, 0
for i in range(len(img3)):
    for j in range(len(img3[1])):
        day_n2_r+=img3[i][j][0]
        day_n2_g+=img3[i][j][1]
        day_n2_b+=img3[i][j][2]
print("day n  red is: ", day_n2_r, "  day n green is: ", day_n2_g, " day n  blue is :  ", day_n2_b)


#WATERING MUST BE DONE IF GREEN CONTENT IN DAY1 IS DECREASED OR RED CONTENT IS INCREASED
if(day_n_g > day_n_r and day_n2_g > day_n2_r):
    if(day_n_g>day_n2_g):
        print("green content decreased so watering and lighting must be done")
    elif(day_n_r<=day_n2_r):
        print("red content increased so watering and lighting must be done")
    else:
        print("plant is healthy")
else:
    print("please change the selected leaf, it has dried.")
    


#READING DAY 10 IMAGE
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
path=r'C:\Users\nvnmu\Desktop\day10.jpg'
img20=cv2.imread(path)
img4 = cv2.cvtColor(img20, cv2.COLOR_BGR2RGB)
plt.imshow(img4)


#CHECKING GREEN CONTENT AND RED CONTENT IN THE LEAF ON DAY 10
day_n3_g, day_n3_r, day_n3_b = 0, 0, 0
for i in range(len(img4)):
    for j in range(len(img4[1])):
        day_n3_r+=img4[i][j][0]
        day_n3_g+=img4[i][j][1]
        day_n3_b+=img4[i][j][2]
print("day n  red is: ", day_n3_r, "  day n green is: ", day_n3_g, " day n  blue is :  ", day_n3_b)


day_n_r=day_n2_r
day_n2_r=day_n3_r
day_n_g=day_n2_g
day_n2_g=day_n3_g
#CHECKING IF THE LEAF IS DRY AND REPLACING IT IF IT IS DRY
if(day_n_g > day_n_r and day_n2_g > day_n2_r):
    if(day_n_g>day_n2_g):
        print("watering and lighting must be done")
    elif(day_n_r<=day_n2_r):
        print("watering and lighting must be done")
    else:
        print("plant is healthy")
else:
    print("please change the selected leaf, it has dried.")


