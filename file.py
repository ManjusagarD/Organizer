import time
import os
import shutil

# Define your file categories
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Code': ['.py', '.js', '.html', '.css', '.java'],
    # Add more categories as needed
}

def organize_files(source_folder):
    # Get list of files in the directory
    files = os.listdir(source_folder)


    for file in files:
        # Ignore directories
        if os.path.isdir(os.path.join(source_folder, file)):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(file)
        
        # Find the correct category for the file
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                # Create category folder if it doesn't exist
                category_folder = os.path.join(source_folder, category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                # Move the file to the correct folder
                shutil.move(os.path.join(source_folder, file), os.path.join(category_folder, file))
                moved = True
                break

        # If the file doesn't match any category, move to 'Others'
        if not moved:
            other_folder = os.path.join(source_folder, 'Others')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(os.path.join(source_folder, file), os.path.join(other_folder, file))

    print("Files organized successfully!")

if __name__ == '__main__':
    source_directory = input("Enter the path of the directory you want to organize: ")
    organize_files(source_directory)
