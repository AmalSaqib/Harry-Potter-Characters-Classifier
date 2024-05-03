from PIL import Image
import os

def find_folder(directory, prefix):
    for item in os.listdir(directory):
    # Check if the item is a directory and starts with the specified prefix
        if os.path.isdir(os.path.join(directory, item)) and item.startswith(prefix):
            return item  # Return the folder name if found
    
    # Return None if no matching folder is found
    return None

def resize_images(input_dir, output_dir):
    # Loop through each image file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.png'):
            prefix = filename.split(' ')[0]
        
            folder = find_folder(output_dir, prefix)
            
            new_directory = output_dir + "/" + folder          
            
            no_of_images = len(os.listdir(new_directory))
            
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
                img_resized.save(os.path.join(new_directory, str(no_of_images) + '.png'))
                
                os.remove(os.path.join(input_dir, filename))
                
# Example usage
input_folder = "./dataset/Collection of data"
output_folder = "./dataset/train"
resize_images(input_folder, output_folder)