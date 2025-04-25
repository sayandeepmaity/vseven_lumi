import os

# Mapping direction names to coordinates in the (x, y, z) system
direction_to_coordinates = {
    'center': (0, 0, 0),
    'front': (0, 0, 1),    # Positive Z direction
    'back': (0, 0, -1),    # Negative Z direction
    'left': (-1, 0, 0),    # Negative X direction
    'right': (1, 0, 0),    # Positive X direction
}

# Define a function to rename the folders and files
def rename_folders_and_files(source_folder):
    # List all gun folders in the root folder
    gun_folders = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]

    # Loop through each gun folder (e.g., ak)
    for gun_folder in gun_folders:
        gun_folder_path = os.path.join(source_folder, gun_folder)
        
        # List all distance folders inside the gun folder (e.g., 0m, 50m, 100m)
        distance_folders = [f for f in os.listdir(gun_folder_path) if os.path.isdir(os.path.join(gun_folder_path, f))]

        for distance_folder in distance_folders:
            distance_folder_path = os.path.join(gun_folder_path, distance_folder)
            
            # Extract the distance in meters (e.g., 50m, 100m, etc.)
            distance = distance_folder.replace('m', '')  # Remove the "m" to get the number
            if distance == '0':
                distance = 0  # Center position for 0m
            
            # List all subfolders (directions: front, back, left, right, center)
            subfolders = [f for f in os.listdir(distance_folder_path) if os.path.isdir(os.path.join(distance_folder_path, f))]

            for subfolder in subfolders:
                # Map the direction to coordinates
                if subfolder.lower() in direction_to_coordinates:
                    direction = subfolder.lower()
                    coordinates = direction_to_coordinates[direction]
                else:
                    # If the direction is not recognized, set to (0, 0, 0)
                    coordinates = (0, 0, 0)
                
                # Create a new folder name based on the coordinates (x, y, z)
                new_folder_name = f"{coordinates[0]}_{coordinates[1]}_{coordinates[2]}_{distance}m"
                new_folder_path = os.path.join(distance_folder_path, new_folder_name)
                
                # Rename the subfolder to the new name
                os.rename(os.path.join(distance_folder_path, subfolder), new_folder_path)

                # List all files in the subfolder and rename them serially
                audio_files = [f for f in os.listdir(new_folder_path) if f.endswith('.mp3')]

                # Rename the files in the folder serially
                for index, file_name in enumerate(audio_files, start=1):
                    old_file_path = os.path.join(new_folder_path, file_name)
                    # Create new file name as a serial number (e.g., 1.mp3, 2.mp3, ...)
                    new_file_name = f"{index}.mp3"
                    new_file_path = os.path.join(new_folder_path, new_file_name)
                    
                    # Rename the file
                    os.rename(old_file_path, new_file_path)

            print(f"Renamed folders and files in '{distance_folder}' under gun '{gun_folder}'")

# Set the path to your root folder containing gun folders
source_folder = r'C:\Users\sayan\Downloads\gun_sound_v2\gun_sound_v2'  # Your folder path
rename_folders_and_files(source_folder)
