from src.youtube import YouTube


class Video:
    def __init__(self, id_video):
        self.__id_video = id_video
        self.__video = YouTube.get_video(self.__id_video)
        self.__title = self.__video['items'][0]['snippet']['title']
        self.__url = f'https://www.youtube.com/watch?v={self.__id_video}'
        self.__views_count = self.__video['items'][0]['statistics']['viewCount']
        self.__likes_count = self.__video['items'][0]['statistics']['likeCount']

    @property
    def id_video(self):
        return self.__id_video

    @property
    def title(self):
        return self.__title

    @property
    def url(self):
        return self.__url

    @property
    def views_count(self):
        return self.__views_count

    @property
    def likes_count(self):
        return self.__likes_count

    def __str__(self):
        return self.__title


class PLVideo(Video):
    def __init__(self, id_video, playlist_id):
        self.__playlist_id = playlist_id
        super().__init__(id_video)

    @property
    def playlist_id(self):
        return self.__playlist_id
