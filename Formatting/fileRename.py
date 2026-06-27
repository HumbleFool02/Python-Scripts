import os

def rename_images(folder_path):
    # Get a list of all JPG files in the folder
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(".jpg")]
    
    # Sort files to maintain order (default is lexicographic order)
    files.sort()
    
    # Rename files sequentially
    for index, filename in enumerate(files, start=1): #Enter the start number as per you
        old_path = os.path.join(folder_path, filename)
        new_filename = f"{index}.jpg"
        new_path = os.path.join(folder_path, new_filename)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

# Example usage
folder_path = "/Users/skynet/Desktop/ScreenShots"  # Change this to your actual folder path
rename_images(folder_path)
