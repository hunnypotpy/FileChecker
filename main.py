import os
import sys
import finder_colors
import notifications

USER_DESKTOP_PATH = os.environ['HOME'] + '/Desktop'


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
        search_path = sys.argv[1]
        print("Searching this location for directories with green label: ")
        print(search_path)
        print("*********************************************************")
        print("Found:")
        search_for_green_labeled_files(search_path)
        print("*********************************************************")
        print("Search complete!")

    elif n == 1:
        print("Please provide a path to search")
    else:
        print("Too many arguments.  If your path has spaces, be sure to wrap it in quotes")
