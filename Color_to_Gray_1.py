import cv2

img = cv2.imread("C:\\Users\\jac13\\OneDrive\\Lenna.jpg")  # 讀取檔案位置
newImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)              # 做成_灰階圖片
cv2.imshow("win",newImg)                                   # 視窗名稱_設為 win
cv2.waitKey(0)

