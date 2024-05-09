import os
import csv

def create_csv(dataset_dir, output_file):
    # Open CSV file for writing
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Image_Path', 'Label'])  # Write header row

        # Iterate through each class directory in the dataset
        for class_name in os.listdir(dataset_dir):
            class_dir = os.path.join(dataset_dir, class_name)

            # Skip non-directory files
            if not os.path.isdir(class_dir):
                continue

            # Iterate through each image file in the class directory
            for img_name in os.listdir(class_dir):
                # Check if the file has a supported image extension
                if not img_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                    continue
                img_path = os.path.join(class_dir, img_name)
                csv_writer.writerow([img_path, class_name])

# Example usage
dataset_directory_train = "train"  # Adjust path to your dataset directory
dataset_directory_test = "test"  # Adjust path to your dataset directory

output_csv_file_train = "train.csv"  # Output CSV file name
output_csv_file_test = "test.csv"  # Output CSV file name


create_csv(dataset_directory_train, output_csv_file_train)
create_csv(dataset_directory_test, output_csv_file_test)
