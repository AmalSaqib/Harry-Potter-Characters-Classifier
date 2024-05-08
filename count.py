import os

input_folder = "./dataset/test"


for item in os.listdir(input_folder):
    folder = os.path.join(input_folder, item)
    no_of_files = len(os.listdir(folder))
    
    print(item, no_of_files)        