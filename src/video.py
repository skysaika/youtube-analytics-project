from src.youtube import YouTube


class Video:
    """Класс Video"""
    def __init__(self, id_video):
        """Инициализатор класса Video"""
        self.__id_video = id_video
        self.__video = YouTube.get_video(self.__id_video)
        try:
            self.__title = self.__video['items'][0]['snippet']['title']
            self.__url = f'https://www.youtube.com/watch?v={self.__id_video}'
            self.__views_count = self.__video['items'][0]['statistics']['viewCount']
            self.__likes_count = self.__video['items'][0]['statistics']['likeCount']
        except IndexError:
            self.__title = None
            self.__url = None
            self.__views_count = None
            self.__likes_count = None

    @property
    def id_video(self):
        """Геттер, возвращает id видео"""
        return self.__id_video

    @property
    def title(self):
        """Геттер, возвращает название видео"""
        return self.__title

    @property
    def url(self):
        """Геттер, возвращает ссылку на видео"""
        return self.__url

    @property
    def views_count(self):
        """Геттер, возвращает количество просмотров"""
        return self.__views_count

    @property
    def likes_count(self):
        """Геттер, возвращает количество лайков"""
        return self.__likes_count

    def __str__(self):
        """Метод возвращает строковый вид"""
        return self.__title


class PLVideo(Video):
    def __init__(self, id_video, playlist_id):
        """Инициализатор класса PLVideo"""
        self.__playlist_id = playlist_id
        super().__init__(id_video)

    @property
    def playlist_id(self):
        """Геттер, возвращает id плейлиста"""
        return self.__playlist_id
