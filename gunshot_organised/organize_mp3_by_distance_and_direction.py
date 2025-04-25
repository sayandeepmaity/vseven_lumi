import os
import shutil
import re

def organize_mp3_files_by_distance_and_direction(source_folder):
    # List all the 'gun' folders
    gun_folders = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]

    # Define a regular expression pattern to extract distance (in meters) and direction
    distance_pattern = re.compile(r'(\d+)\s?m')  # Looks for "XXm" pattern (e.g., 1m, 2m)
    direction_keywords = ['front', 'back', 'left', 'right']

    for gun_folder in gun_folders:
        gun_folder_path = os.path.join(source_folder, gun_folder)
        
        # List all MP3 files in the 'gun' folder
        mp3_files = [f for f in os.listdir(gun_folder_path) if f.endswith('.mp3')]

        for mp3_file in mp3_files:
            # Search for the distance (in meters) in the filename
            distance_match = distance_pattern.search(mp3_file)
            if distance_match:
                distance = distance_match.group(1)  # Extract the distance (in meters)
            else:
                distance = 'unknown'  # If no distance is found, mark it as 'unknown'

            # Check for direction keywords (e.g., front, back, left, right) in the filename
            direction = 'unknown'
            for keyword in direction_keywords:
                if keyword in mp3_file.lower():
                    direction = keyword
                    break

            # Create the folder for the distance if it doesn't exist
            distance_folder = os.path.join(gun_folder_path, distance + 'm')
            if not os.path.exists(distance_folder):
                os.makedirs(distance_folder)

            # Create the subfolder for the direction inside the distance folder
            direction_folder = os.path.join(distance_folder, direction)
            if not os.path.exists(direction_folder):
                os.makedirs(direction_folder)

            # Move the file into the respective subfolder
            source_path = os.path.join(gun_folder_path, mp3_file)
            destination_path = os.path.join(direction_folder, mp3_file)
            shutil.move(source_path, destination_path)

        print(f"Files in folder '{gun_folder}' have been organized by distance and direction.")

# Set the path to your root folder containing gun folders
source_folder = r'C:\Users\sayan\Downloads\gun_sound_v2\gun_sound_v2'  # Your folder path
organize_mp3_files_by_distance_and_direction(source_folder)
