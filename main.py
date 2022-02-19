# import os
import finder_colors

TESTFOLDERPATH = '/Users/edgarcia/Desktop/vxrail.pdf'

# TODO: get foldername from user or set the foldername in env vars

# nagivate to folder

# look for green colored files in folder

folder_color = finder_colors.get(TESTFOLDERPATH)
print(folder_color)

'''for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file colored with('green')
            print (root+'/'+str(file))
        else:
            print('File not here!')'''

# alert if there is one
# check again in 10 minutes


