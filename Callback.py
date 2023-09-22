import cv2

def to_gray(img):
    print("to_gray")
    newImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",newImg)

def to_rgb(img):
    cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("rgb",img)

def template(algorithm):
    print("hello")
    img = cv2.imread("C:\\Users\\jac13\\OneDrive\\Lenna.jpg")
    algorithm(img)
    cv2.waitKey(0)

template(to_gray)

def template1():
    print("hello")
    img = cv2.imread("C:\\Users\\jac13\\OneDrive\\Lenna.jpg")
    cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",img)

def template2():
    print("hello")
    img = cv2.imread("C:\\Users\\jac13\\OneDrive\\Lenna.jpg")
    cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",img)
