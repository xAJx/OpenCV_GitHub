import cv2
a = [[123,34,57,62,"cat"],[12,85,145,32,"dog"]]
b = [123,34,57,62,"cat"]

img = cv2.imread("C:\\Users\\jac13\\OneDrive\\Lenna.jpg")

def draw_text(i,name,img): 
    newString =  str(i) + '.' + name
    print(newString)
    position = (10,90 + 30*i)  # 設定字體 在圖檔中 的 x, y  軸 位置
    size = 1                   # 字體大小 尺吋 設為 1
    color = (0,255,0)          # 將 文字內容 的 筆觸-線條顏色 設為 綠色
    lineWidth = 1              #    文字       筆觸 的厚度 設為 1
    cv2.putText(img,newString,position,cv2.FONT_HERSHEY_SIMPLEX,size,color,lineWidth)   # 設定 文字內容_相關參數

def draw_rectangle(x, img):
    point1 = (x[0],x[1])
    point2 = (x[2],x[3])
    # position = (30,70 )
    color = (0,0,255)       # 將長方形 畫筆筆觸 的線條顏色 設為 紅色
    thickness = 1           #   長方形    筆觸 的厚度 設為 1
    cv2.rectangle(img,point1,point2,color,thickness)
    #cv2.rectangle(img,point1,point2,position,color,thickness)

def show_result(img,a,isSave):
    i = 0
    
    for x in a:
        i += 1
        draw_rectangle(x, img) 
        draw_text(i,x[4],img)

        cv2.imshow(str(i)+"Test",img)
        
        if isSave:
            cv2.imwrite(str(i) + "Product.jpg",img)

    cv2.waitKey(0)
show_result(img,a,True)





    


 