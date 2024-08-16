import json
from load_files import *
from list_all import *
from save_data import *
from updated import*
from add_values import*
from delete_video import *



videos = load_files()


def main():
    while True:
        
        print("\n ************* Youtube manager **************")
        print("\n Select the Option you want ")
        print("1. List all the youtube Videos")
        print("2. Add Youtube Videos")
        print("3.Update Youtube Videos")
        print("4. Delete Youtube Videos")
        print("5.Exit the Videos")
        chioce = int(input("Print the desired option from above : "))

        match chioce:
            case 1:
                list_all_youtube_videos(videos)
            case 2:
                add_videos(videos)
            case 3:
                list_all_youtube_videos(videos)    
            case 4:
                list_all_youtube_videos(videos)
            case 5:
                break
            case _:
                print("ERROR 404")

if __name__ == "__main__":
    main()

