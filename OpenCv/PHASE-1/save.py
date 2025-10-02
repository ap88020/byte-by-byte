import cv2

image = cv2.imread("PHASE-1/G_2.jpg")

if image is not None:
    success = cv2.imwrite("output.png",image)
    if success:
        print("image saved successfuly as 'output.png'") 
    else:
        print("image dosen't save")
else:
    print("could not load image")

