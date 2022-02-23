import os
import sys
from time import sleep
import finder_colors
import notifications

USER_DESKTOP_PATH = os.environ['HOME'] + '/Desktop'
# check every 30 minutes for 4 hours
INTERVAL_IN_MINUTES = 30
NUMBER_OF_INTERVALS = 8


def search_for_green_labeled_files(folder_to_search):
    for root, dirs, files in os.walk(folder_to_search, topdown=True):
        for item in dirs:
            obj_path = (root + '/' + str(item))
            obj_color = finder_colors.get(obj_path)
            if obj_color == 'green':
                print(obj_path)
                notifications.desktop_popup("Green Label Found", obj_path)


if __name__ == "__main__":
    n = len(sys.argv)
    if n == 2:
        x = NUMBER_OF_INTERVALS
        while x != 0:
            search_path = sys.argv[1]
            print("Searching this location for directories with green label: ")
            print(search_path)
            print("*********************************************************")
            print("Found:")
            search_for_green_labeled_files(search_path)
            print("*********************************************************")
            print("Search complete!")
            x = x-1
            print(x)
            sleep(INTERVAL_IN_MINUTES * 60)

    elif n == 1:
        print("Please provide a path to search")
    else:
        print("Too many arguments.  If your path has spaces, be sure to wrap it in quotes")
