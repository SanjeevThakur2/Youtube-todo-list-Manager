import json

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)