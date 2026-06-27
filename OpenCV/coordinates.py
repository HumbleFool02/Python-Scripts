import cv2 
import numpy as np

#List to store coordinate
coordinates = []

# Callback function to get mouse click coordinates
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button clicked
        coordinates.append((x, y))
        print(f"Clicked at (x={x}, y={y})")

img_path = '/Users/skynet/Repositorites/OpenCV/data/parking_image.png'
image = cv2.imread(img_path)

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', get_coordinates)

# Display the image
cv2.imshow('Image', image)

# Print all the stored coordinates
print("Stored Coordinates:")

for coord in coordinates:
    print(f"({coord[0]}, {coord[1]})")

# File path for the text document
file_path = 'coordinates.txt'  # Replace with the desired file path

# Open the file in write mode and write the list elements to it
with open(file_path, 'w') as file:
    for item in coordinates:
        x, y = coord
        file.write(f"{x},{y}\n")


while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()

with open(file_path, 'w') as file:
    for coord in coordinates:
        x, y = coord
        file.write(f"{x},{y}\n")