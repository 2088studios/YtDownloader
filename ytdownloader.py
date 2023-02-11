# Library Here -> https://pytube.io/en/latest/

#TODO Figure out how to choose download quality (from ???-4k)
#TODO Figure out how to get this into an executable file
#TODO Add exception blocks

#Libraries to get YouTube video and users' Downloads folder path
from pytube import YouTube
from pathlib import Path

#Gets video URL from user
url = input('Hello, please input video URL\n')

#Creates YouTube object and assigns users' Downloads folder path
video = YouTube(url)
download_path = str(Path.home() / "Downloads")

#Prints video data
print("Video Title: ", video.title)
print("Views: ", video.views)

#Gets highest quality video (up to 720 as of now) and then downloads it
dv = video.streams.get_highest_resolution()
dv.download(download_path)

#TODO check if video has already been downloaded
#if yt.title==:
#    print("There is already a video with that name. Cannot download video")

print("Video has been downloaded successfully!")