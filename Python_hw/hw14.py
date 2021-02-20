import cv2 
import numpy as np

#從本地端抓取影片
vid_control = cv2.VideoCapture("h3.mp4")

#進入迴圈並判斷是否等於True
while vid_control.isOpened() == True:
  #影片的讀取
  vid_on,video = vid_control.read()
  #判斷 影片是否成功被讀取，如果判斷為True，就執行下面的程式
  if vid_on == True:
    #抓取影片中的藍色區塊(筆的部分)，把偏黃色的地方去掉
    video2 = cv2.inRange(video,(90,0,0),(255,70,100))
    #對影片做膨脹處理
    video2 = cv2.dilate(video2,np.ones((30,30)))
    #複製影片2的(像素，高、寬)
    video3 = video2.copy()
    #秀出影片2
    cv2.imshow("M1",video2)
    #取得輪廓
    a , b = cv2.findContours(video2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    #繪製輪廓
    cv2.drawContours(video3, a, -1, (0,0,255), 1)
    #設定d迴圈，範圍為a
    for d in a:
      #取得包覆d輪廓點的最小正矩形，X座標, Y座標, 寬度, 高度
      x, y, w, h = cv2.boundingRect(d)
      #繪製矩形(圖像變數(video), 矩形左上點(x+w), 矩形右下點(y+h), 顏色(紅), 線粗細3)
      cv2.rectangle(video, (x,y) , (x+w , y+h), (0,0,255), 3)
      #秀出處理完後的影片
    cv2.imshow("M2",video)
    #影片偵數存入Key
    key = cv2.waitKey(33)
    #按任意鍵結束影片
    if key != -1:
      break
  else:
    break
#關閉所有視窗一定要有的東西
cv2.destroyAllWindows()












# while(cap.isOpened()):
#   # 讀取一幅影格
#   ret, frame = cap.read()

#   # 若讀取至影片結尾，則跳出
#   if ret == False:
#     break

#   # 模糊處理
#   blur = cv2.blur(frame, (4, 4))

#   # 計算目前影格與平均影像的差異值
#   diff = cv2.absdiff(avg, blur)

#   # 將圖片轉為灰階
#   gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

#   # 篩選出變動程度大於門檻值的區域
#   ret, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

#   # 使用型態轉換函數去除雜訊
#   kernel = np.ones((5, 5), np.uint8)
#   thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
#   thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

#   # 產生等高線
#   cntImg, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#   for c in cnts:
#     # 忽略太小的區域
#     if cv2.contourArea(c) < 2500:
#       continue

#     # 偵測到物體，可以自己加上處理的程式碼在這裡...

#     # 計算等高線的外框範圍
#     (x, y, w, h) = cv2.boundingRect(c)

#     # 畫出外框
#     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#   # 畫出等高線（除錯用）
#   cv2.drawContours(frame, cnts, -1, (0, 255, 255), 2)

#   # 顯示偵測結果影像
#   cv2.imshow('frame', frame)