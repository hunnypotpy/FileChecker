import os
import sys
import finder_colors
import notifications

USER_DESKTOP_PATH = os.environ['HOME'] + '/Desktop'


def search_for_green_labeled_files(folder_to_search):
    for root, dirs, files in os.walk(folder_to_search, topdown=True):
        for file in files:
            file_path = (root + '/' + str(file))
            file_color = finder_colors.get(file_path)
            if file_color == 'green':
                print(file_path)
                notifications.desktop_popup("Green Label Found", file_path)


if __name__ == "__main__":
    n = len(sys.argv)
    if n == 2:
        search_path = sys.argv[1]
        print("Searching this location: ")
        print(search_path)
        print("***********************")
        search_for_green_labeled_files(search_path)
    elif n == 1:
        print("Searching this location: ")
        print(USER_DESKTOP_PATH)
        print("***********************")
        search_for_green_labeled_files(USER_DESKTOP_PATH)
    else:
        print("Too many arguments.  If your path has spaces, be sure to wrap it in quotes")
