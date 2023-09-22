import cv2

circleRadius = 1
def update(x):
    print(x)
    global circleRadius    #def內不會影響外面，但加上global，就可以改變外部結果。例如這邊若令x=2，circleRadius會從原本的1更新為2。
    circleRadius = x
px = 1
py = 1
def update1(x):
    global px
    px = x

def update2(y):
    global py
    py = y


# img = cv2.imread(("C:\\Users\\jac13\\OneDrive\\Lenna.jpg"))  # 這是 絕對路徑 比較長，如果設錯位置，會造成 copy 指令錯誤
img = cv2.imread(("C:Lenna.jpg"))
cv2.namedWindow("win")
cv2.createTrackbar("bar","win",0,100,update)  # 滑桿名稱、視窗名稱，最小值，最大值，滑桿數值改變時要執行的函式
cv2.createTrackbar("bar1","win",0,100,update)
cv2.createTrackbar("bar2","win",0,100,update)

# cv2.setTrackbarPos('滑桿名稱','視窗名稱', val)   #　設置滑動條位置＿（滑桿名稱,視窗名稱，位置）

color=(255,0,0)
thickness = 2
while True:
    circleImg = img.copy()
    center = (px,py)
    cv2.circle(circleImg,center,circleRadius,color,thickness)
    cv2.imshow("win",circleImg)
    x = cv2.waitKey(100)
    if x == 27:
        break



