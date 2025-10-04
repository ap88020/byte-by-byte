import cv2

image = cv2.imread("G_2.jpg")

if image is None:
    print("oops! not found image")
else:
    print("images loaded successfully")
    
    pt1 = (50,50)
    pt2 = (250,200)

    color = (153,255,255)
    thickness = 4

    cv2.rectangle(image,pt1,pt2,color,thickness)

    cv2.imshow("rectangle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()