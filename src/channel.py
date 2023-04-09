import json


from dotenv import load_dotenv


from settings import ENV_FILE


load_dotenv(ENV_FILE)


class Channel:
    """Класс для каналов"""
    def __init__(self, channel_id: str, Youtube=None) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__channel = Youtube.get_channel(self.__channel_id)
        self.__title = self.__channel['items'][0]['snippet']['title']
        self.__description = self.__channel['items'][0]['snippet']['description']
        self.__url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.__subscribers_count = int(self.__channel['items'][0]['statistics']['subscriberCount'])
        self.__video_count = int(self.__channel['items'][0]['statistics']['videoCount'])
        self.__views_count = int(self.__channel['items'][0]['statistics']['viewCount'])

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__channel, indent=2, ensure_ascii=False))

    @property
    def title(self) -> str:
        """Геттер возвращает название канала."""
        return self.__title

    @property
    def description(self) -> str:
        """Геттер возвращает описание канала."""
        return self.__description

    @property
    def url(self) -> str:
        """Геттер возвращает url канала."""
        return self.__url

    @property
    def subscribers_count(self) -> int:
        """Геттер возвращает количество подписчиков канала."""
        return self.__subscribers_count

    @property
    def video_count(self) -> int:
        """Геттер возвращает количество видео канала."""
        return self.__video_count

    @property
    def views_count(self) -> int:
        """Геттер возвращает количество просмотров канала."""
        return self.__views_count

    @property
    def channel_id(self) -> str:
        """Геттер возвращает id канала."""
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Сеттер возвращает id канала."""
        raise AttributeError("property 'channel_id' of 'Channel' object has no setter")

    def to_json(self, filename) -> None:
        """Метод возвращает в json значения атрибутов экземпляра Channel."""
        data = {
            'channel_id': self.__channel_id,
            'title': self.__title,
            'description': self.__description,
            'url': self.__url,
            'subscribers_count': self.__subscribers_count,
            'video_count': self.__video_count,
            'views_count': self.__views_count
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def __str__(self) -> str:
        """Метод возвращает строку с данными канала."""
        return f'{self.__title} ({self.__url})'

    def __add__(self, other: 'Channel') -> int:
        """Метод складывает два канала Channel по количеству подписчиков"""
        return self.__subscribers_count + other.__subscribers_count

    def __sub__(self, other: 'Channel') -> int:
        """Метод вычитает канал Channel по количеству подписчиков"""
        return self.__subscribers_count - other.__subscribers_count

    def __ge__(self, other: 'Channel') -> bool:
        """Метод сравнивает два канала Channel по количеству подписчиков"""
        return self.__subscribers_count >= other.__subscribers_count
