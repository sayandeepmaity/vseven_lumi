import os
import shutil

def organize_mp3_files(source_folder):
    # List all files in the source folder
    mp3_files = [f for f in os.listdir(source_folder) if f.endswith('.mp3')]

    # Create a folder for each group based on a prefix (you can customize this logic)
    for mp3_file in mp3_files:
        # Example: split the filename based on the first word (you can customize this logic)
        group_name = mp3_file.split('_')[0]  # Split by the first underscore or any other delimiter
        
        # Create a folder for the group if it doesn't exist
        group_folder = os.path.join(source_folder, group_name)
        if not os.path.exists(group_folder):
            os.makedirs(group_folder)
        
        # Define the path to move the file
        source_path = os.path.join(source_folder, mp3_file)
        destination_path = os.path.join(group_folder, mp3_file)
        
        # Move the file to the new folder
        shutil.move(source_path, destination_path)

    print("Files have been organized successfully.")

# Set the path to your folder containing MP3 files
source_folder = r'C:\Users\sayan\Downloads\gun_sound_v2\gun_sound_v2'  # Your folder path
organize_mp3_files(source_folder)
