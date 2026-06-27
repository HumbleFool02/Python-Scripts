import cv2
import numpy as np

img_path = 'data/3.jpg'
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

# Print the list of square coordinates
print("List of Square Coordinates:")
for square in squares:
    print(square)


b_height, b_width, b_channels = image.shape
# Create a black image as a NumPy array
black_image = np.zeros((b_height, b_width, b_channels), dtype=np.uint8)

# Draw the squares on the black image
for square in squares:
    start_x, start_y = square[0]
    end_x, end_y = square[1]
    cv2.rectangle(black_image, (start_x, start_y), (end_x, end_y), (255, 255, 255), -1)

# Display the image with the drawn squares
cv2.imshow('Original Image', image)
cv2.imshow('Image with Squares', black_image)

output_masked_image = 'data/masked1.jpg'
cv2.imwrite(output_masked_image, black_image)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
