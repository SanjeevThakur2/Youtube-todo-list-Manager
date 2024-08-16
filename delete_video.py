from list_all import *
from save_data import *

def delete_videos(videos):

    print('*' * 80)
    print("\n You are in Delete below are the options")

    list_all_youtube_videos(videos)

    index = int(input("Enter the video Number you want to delete"))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index Given")