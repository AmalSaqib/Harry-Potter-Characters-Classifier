from PIL import Image
import os

def resize_images(input_dir, output_dir):
    img_no = 1
    
    # # Create output directory if it doesn't exist
    # os.makedirs(output_dir, exist_ok=True)
    
    # Loop through each image file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Open the image file
            with Image.open(os.path.join(input_dir, filename)) as img:
                width, height = img.size
                if width > height:
                    new_width = 256
                    new_height = int((new_width / width) * height)
                else:
                    new_height = 256
                    new_width = int((new_height/height) * width)
                    
                # Resize the image
                img_resized = img.resize((new_width, new_height))
                
                # Save the resized image to the output directory
                img_resized.save(os.path.join(output_dir, str(img_no) + '.png'))
                img_no += 1

# Example usage
input_folder = "./dataset/train/Hedwig"
output_folder = "./dataset/train/Hedwig"

resize_images(input_folder, output_folder)