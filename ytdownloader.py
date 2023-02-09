# Coding Tutorial Here -> https://youtu.be/vEQ8CXFWLZU?t=320
# Library Here -> https://pytube.io/en/latest/

#TODO Figure out how to choose download quality (from ???-4k)
#TODO Figure out how to merge audio and video again IF THIS HAPPENS
#TODO Figure out how to get this into an executable file

#imports
from pytube import YouTube
from sys import argv

#
link = argv[1]
yt = YouTube(link)

#
print("Video Title: ", yt.title)

#
print("Views: ", yt.views)

#
yd = yt.streams.get_highest_resolution()

#TODO Get to download to specific path
yd.download(output_path="C:\Users\isali\Downloads")
