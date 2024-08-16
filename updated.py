from save_data import *
from list_all import*

def update_videos(videos):
    print('*' * 80)
    print("\n You are in Update select the option you want to update")
    
    list_all_youtube_videos(videos)
    index = int(input("Enter the video Number you want to update"))

    if 1 <= index <= len(videos):
        enter_new_name = input("Enter Name")
        enter_new_time = input("Enter Time")
        videos[index - 1] = {'name': enter_new_name , 'time':enter_new_time}
        save_data_helper(videos)
    else:
        print("Invalid index Given")