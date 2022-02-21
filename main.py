import os
import finder_colors

TESTFOLDERPATH = '/Users/edgarcia/Desktop/Timing'

# TODO: get server volume name to be searched, user input or set in env vars (e.g. duncanvill_production)
# SERVER_VOLUME_NAME =
# TODO: get top-level folder name to search (e.g. Timing)
# TOP_LEVEL_FOLDER_NAME =

# TODO: walk all folders with TOP_LEVEL_FOLDER_NAME and look for green colored files in folder

for root, dirs, files in os.walk(TESTFOLDERPATH, topdown=True):
    # look for green labeled files
    for file in files:
        file_path = (root + '/' + str(file))
        file_color = finder_colors.get(file_path)
        if file_color == 'green':
            print(file_path)
            # alert if any green labels are found
