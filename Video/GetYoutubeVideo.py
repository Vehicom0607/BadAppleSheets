import pytube


def download_youtube_video():
    link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    stream.download()


download_youtube_video()