import cv2
import numpy as np

im1=cv2.imread("h2.png",1)
im2=np.full(im1.shape,(255,255,0),np.uint8)
#相加後可以將紅色文字(0,0,255)變為白色 背景的顏色幾乎保持不變
im3=cv2.bitwise_not(im1+im2)
#bitwise_not將白色文字變為黑色 背景變為互補色
im4=cv2.cvtColor(im3,cv2.COLOR_BGR2GRAY)
#轉為灰階 文字的部分為0 其他背景為不為0的灰色
im5=cv2.multiply(im4,(255))
#將所有元素乘255倍 灰色的背景變為白色 黑色因為是0保持不變
cv2.imshow("M2",im1)
cv2.imshow("im2",im5)
cv2.waitKey(0)
cv2.destroyAllWindows()