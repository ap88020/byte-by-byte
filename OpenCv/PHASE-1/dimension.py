import cv2 

image = cv2.imread("PHASE-1/G_2.jpg")

if image is not None:
    h , w , c = image.shape
    print(f"Loaded successfully\n{h}\n{w}\n{c}")
else:
    print("could not found image")


