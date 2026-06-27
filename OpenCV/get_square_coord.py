import cv2
import time 

# List to store the coordinates of squares
squares = [] #[(start_x, start_y), (end_x, end_y)]
fin_squares = [] #[(x, y, w, h)]

# Global variables to store the starting and ending coordinates of the square
start_x, start_y, end_x, end_y = -1, -1, -1, -1
drawing = False

# Callback function to draw the square and get its dimensions
def draw_square(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
        drawing = True
        time.sleep(0.8)
    elif event == cv2.EVENT_RBUTTONDOWN:
        end_x, end_y = x, y
        drawing = False
        # Append the coordinates to the list when the square is complete
        squares.append(((start_x, start_y), (end_x, end_y)))

# Provide the file path of the image you want to open
image_path = 'data/3.jpg'  # Replace with the actual image file path

# Read the image using OpenCV
image = cv2.imread(image_path)
file_path = 'coordinates.txt'  # Replace with the desired file path

# Check if the image was successfully loaded
if image is not None:
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', draw_square)

    while True:
        # Create a copy of the original image to draw the squares
        display_image = image.copy()

        # Draw all the squares from the list on the copy of the image
        for square in squares:
            start_pt, end_pt = square
            cv2.rectangle(display_image, start_pt, end_pt, (0, 255, 0), 2)

        # Show the image with the squares
        cv2.imshow('Image', display_image)

        # Wait for a key press
        key = cv2.waitKey(1) & 0xFF

        # Press 'q' to quit
        if key == ord('q'):
            break
        # Press 'd' to get the dimensions of all squares
        elif key == ord('d') and not drawing:
            for square in squares:
                start_x, start_y = square[0]
                end_x, end_y = square[1]
                width = abs(end_x - start_x)
                height = abs(end_y - start_y)
#                fin_squares.append((start_x, start_y, width, height))
                print(f"Square dimensions: {width}x{height} pixels")


    cv2.destroyAllWindows()

#     with open(file_path, 'w') as file:
# #        for coord in fin_squares:
#         for coord in squares:
#             x, y, w, h = coord
#             file.write(f"{x},{y},{w},{h}\n")

    with open(file_path, 'w') as file:
        for square in squares:
            start_x, start_y = square[0]
            end_x, end_y = square[1]
            file.write(f"{start_x},{start_y},{end_x},{end_y}\n")


else:
    print(f"Error: Image not found or cannot be opened at '{image_path}'")
