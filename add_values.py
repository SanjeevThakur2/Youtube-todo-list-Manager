from save_data import *
from list_all import*
def add_videos(videos):
    print('*' * 80)
    print("\n You are in add section please add video and dont forget the duration" )


    name = input("Enter Youtube Name: ")
    time = input("Enter Video Time:  ")
    videos.append({'name': name , 'time': time })
    save_data_helper(videos)