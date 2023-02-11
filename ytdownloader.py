# Library Here -> https://pytube.io/en/latest/

#TODO Figure out how to choose download quality (from ???-4k)
#TODO Figure out how to get this into an executable file
#TODO Add exception blocks
#TODO Add way to download multiple videos back to back
#TODO check if video has already been downloaded
#if yt.title==:
#    print("There is already a video with that name. Cannot download video")

#Libraries to get YouTube video and users' Downloads folder path
from pytube import YouTube
from pathlib import Path
import time

download_path = str(Path.home() / "Downloads")

#Function that downloads the YouTube video
def main():
    #Gets video URL from user
    url = input('Hello, please input video URL\n')

    #Creates YouTube object and assigns users' Downloads folder path
    video = YouTube(url)

    #Prints video data
    print("Video Title: ", video.title)
    print("Views: ", video.views)
    print('Downloading...')

    #Gets highest quality video (up to 720 as of now) and then downloads it
    dv = video.streams.get_highest_resolution()
    dv.download(download_path)

    print("Video has been downloaded successfully!")
    anotherVideo()

#Asks user if they want to download another video
def anotherVideo():
    k = input('Would you like to download another video? (Y/N)\n')

    #User wants to download another
    if (k=='Y' or 'y'):
        main()

    #User doesn't want to download another
    elif(k=='N' or 'n'):
        print('Thank you for using the downloader.')
        print('It will automatically close in 10 seconds.')
        time.sleep(10)

    #Incorrect input
    else:
        anotherVideo()

main()