import cv2
import numpy as np
from PIL import ImageFont,ImageDraw, Image

w=500
h=300

p=int((w-h)/2)

h0=[]
h0.append(0)
w0=[]
w0.append(p)

exit_flag=False

while True:
	for i in range((w-w0[0])*2):
		if i<(w-p):
			print(h0[i])
			m1=np.full((h,w,3),(255,255,255),np.uint8)
			cv2.rectangle(m1,(h0[i],p),(w0[i],w-h),(255,0,0),-1)	
			h0.append(h0[i]+1)
			w0.append(w0[i]+1)
		else:
			print(h0[i])
			m1=np.full((h,w,3),(255,255,255),np.uint8)
			cv2.rectangle(m1,(h0[i],p),(w0[i],w-h),(255,0,0),-1)	
			h0.append(h0[i]-1)
			w0.append(w0[i]-1)
		cv2.imshow("M1",m1)
		k=cv2.waitKey(10)
		if k!=-1:
			exit_flag=True
			break
	if exit_flag:
		break
cv2.destroyAllWindows()
