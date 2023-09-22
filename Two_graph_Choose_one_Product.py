# png 不損圖，jpg 會壓縮到圖檔
import cv2
a = []             
a.append("C:\\Users\\jac13\\OneDrive\\logo.jpg")   # 將 logo圖 放進 a 串列    
a.append("C:\\Users\\jac13\\OneDrive\\Lenna.jpg")  # 將 Lenna圖 放進 a 串列

value = int(input("please enter 1 or 2" '\n'))     # 選擇輸入數值 1  or 2 

img = cv2.imread(a[value-1])                       # 設定要選擇讀取的圖片，[串列 從 0 開始，所以 value 值要減一開始]

cv2.imshow("Choose_Grapht",img)  
cv2.waitKey(0)
