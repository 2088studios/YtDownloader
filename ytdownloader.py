# Library Here -> https://pytube.io/en/latest/

# TODO How to choose download quality (from ???-4a)
# TODO Run on windows[X] and macos[]
# TODO Add exception blocas for downloaded video
# Video already downloaded[]
#
# TODO See if You can download audio and not video

# Checa if video has already been downloaded
# if yt.title==:
#    print("There is already a video with that name. Cannot download video")

# Libraries to get YouTube video and users' Downloads folder path
from pytube import YouTube
from pathlib import Path
import time

download_path = str(Path.home() / "Downloads")


def main():
    print("Hello and welcome to YtDownloader! :)")
    getURL()


def getURL():
    # Gets video URL from user
    url = 'a'

    # TODO add script if a URL insn't provided (close but can still breaa if input is just http:/)
    while not url.lower().startswith("https://www.youtube.com/"):
        url = input(
            'Please input a valid video URL "https://www.youtube.com/..."\n')

    # Creates YouTube object and assigns users' Downloads folder path
    video = YouTube(url)

    # Prints video data
    print("Video Title: ", video.title)
    print("Views: ", video.views)
    chooseDownload(video)


def chooseDownload(video):
    c = input('Press [V] for video and audio. Or [A] for audio only\n')
    # Video and audio
    if (c.lower() == 'v'):
        videoAndAudio(video)

    # Audio only
    elif (c.lower() == 'a'):
        audioOnly(video)

    # Incorrect input
    else:
        chooseDownload()


def videoAndAudio(video):
    # Gets highest quality video (up to 720 as of now) and then downloads it
    dv = video.streams.get_highest_resolution()
    dv.download(download_path)

    print("Video has been downloaded successfully!")
    anotherVideo()


def audioOnly(video):
    da = video.streams.get_audio_only()
    da.download(download_path)
    print("Audio has been downloaded successfully!")
    anotherVideo()


def anotherVideo():
    a = input('Would you like to download another video? (Y/N)\n')

    # User wants to download another
    if (a.lower() == 'y'):
        getURL()

    # User doesn't want to download another
    elif (a.lower() == 'n'):
        closeProgram()

    # Incorrect input
    else:
        anotherVideo()


def closeProgram():
    print('Thank you for using YtDownloader!')
    print('It will automatically close in 10 seconds.')
    time.sleep(10)


main()
