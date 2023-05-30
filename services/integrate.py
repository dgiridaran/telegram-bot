from downloders.youtube_downloder import Youtube


def download_file(url:str):
    if 'https://you' in url:
        u_file = Youtube(url)
        title = u_file.video_title()
        dow=u_file.download()
        return title