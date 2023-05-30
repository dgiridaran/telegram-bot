from pytube import YouTube
from services.name_generator import generate_new_name


class Youtube:
    def __init__(self,link):
        self.link = link
        self.youtubeobject = YouTube(self.link)
        self.youtubeobject.title = generate_new_name(7)

    def video_title(self):
        title = self.youtubeobject.title
        return title

    def download(self):
        # youtubeObject = YouTube(link)
        youtubeObject = self.youtubeobject.streams.get_highest_resolution()
        try:
            youtubeObject.download()
        except:
            print("An error has occurred")
        print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
# u = Youtube(link)
# print(u.video_title())
# u.download()

# RDJ acting like Tony Stark