from downloders.youtube_downloder import Youtube
from downloders.instagram_dow import Instagram

def download_file(url:str):
    if 'https://you' in url:
        u_file = Youtube(url)
        title = u_file.video_title()
        dow=u_file.download()
        return (title,'.mp4')
    elif 'https://www.instagram' in url:
        i_file = Instagram(url)
        title = i_file.get_title
        dow = i_file.save_media_file()
        return (title,dow)
