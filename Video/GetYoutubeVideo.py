import pytube


def download_youtube_video():
    link = "https://www.youtube.com/watch?v=FtutLA63Cp8"
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    stream.download()


download_youtube_video()