#import
import os

#nagivate to folder

#determine type of file to be looking for
#if (.jpg) in folder
#print (file is here!)
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file ends with('.jpg')
            print (root+'/'+str(file))
        else:
            print('File not here!')


#else no (.jpg)
#print (file is missing!)

#check folder again
#determine time interval
