import instaloader
import requests
from services.name_generator import generate_new_name

class Instagram:
    def __init__(self, url:str):
        self.url = url
        self.L = instaloader.Instaloader()
        self.get_title = generate_new_name(7)

    def get_id(self):
        if 'reel' in self.url:
            id = self.url.split('reel/')[1].split('/')[0]
        else:
            id = self.url.split('p/')[1]
            id = id.split('/')[0]
        return id
    
    def get_url(self):
        id = self.get_id()
        post = instaloader.Post.from_shortcode(self.L.context, id)
        photo_url = post.url   # this will be post's thumbnail (or first slide)
        video_url = post.video_url  # if post.is_video is True then it wi
        if video_url:
            return (video_url,'.mp4')
        elif photo_url:  
            return (photo_url,'.png')
        
    def save_media_file(self):
        media_url = self.get_url()
        data = requests.get(media_url[0])

    #  Download the data behind the URL
    # response = requests.get(video_url)
        
    #  Open the response generated into a new file in your local called image.jpg
        with open(f"{self.get_title}{media_url[1]}", "wb") as file:
            file.write(data.content)
        return media_url[1]
