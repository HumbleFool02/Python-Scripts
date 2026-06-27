import cv2
import numpy as np

img_path = '/Users/skynet/Repositorites/OpenCV/data/parking_image.png'
image = cv2.imread(img_path)

# File path for the text document containing square coordinates
file_path = 'coordinates.txt'  # Replace with the actual file path

# List to store the coordinates of squares
squares = []

# Read the coordinates from the text file and store them in the list
try:
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by commas to get individual coordinate values
            start_x, start_y, end_x, end_y = map(int, line.strip().split(','))
            square_coordinates = ((start_x, start_y), (end_x, end_y))
            squares.append(square_coordinates)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

for i, square in enumerate(squares):
    start_x, start_y = square[0]
    end_x, end_y = square[1]

    # Crop the square from the original image
    cropped_square = image[start_y:end_y, start_x:end_x]

    # File path for saving the cropped square
    output_path = f'data/cropped_cars/cropped_square_{i}.jpg'

    # Save the cropped square
    cv2.imwrite(output_path, cropped_square)


while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
