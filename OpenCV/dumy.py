import cv2

img_path = '/Users/skynet/Repositorites/OpenCV/data/parking_image.png'
image = cv2.imread(img_path)

height , weight, channels = image.shape
print(height)
print(weight)
print(channels)