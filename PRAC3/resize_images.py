from PIL import Image
import os

# Set the input and output directories
input_folder = 'input_images'
output_folder = 'output_images'

# Set the desired resolution (width, height)
resize_width = 640
resize_height = 480

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over each image in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Process only image files
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # Resize the image
        img_resized = img.resize((resize_width, resize_height))
        
        # Save the resized image in the output folder
        img_resized.save(os.path.join(output_folder, filename))
        print(f"Resized image saved: {filename}")
