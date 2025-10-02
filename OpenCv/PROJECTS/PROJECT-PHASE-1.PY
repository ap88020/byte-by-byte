import cv2

image = cv2.imread("PROJECTS/G_2.jpg")

if image is not None:
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    show = input("To show this image write yes : ")
    save = input("To save this write yes : ")
    if(show == "yes"):
        cv2.imshow("new_gray",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    if(save == "yes"):
        success = cv2.imwrite("new_gray_project.png",gray)
        if(success):
            print("image saved successfully as 'new_gray_project.png'")
else:
    print("Image could not found")


