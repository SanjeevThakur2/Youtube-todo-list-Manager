def list_all_youtube_videos(videos):

    print('*' * 80)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. video name : {video['name']} and Duration : {video['time']}")