import json
import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

from settings import ENV_FILE
from src.utils import print_info

load_dotenv(ENV_FILE)



class Channel:
    """Класс для ютуб-канала"""
    __api_key: str = os.getenv('API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__channel = self.__youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.__title = self.__channel['items'][0]['snippet']['title']
        self.__description = self.__channel['items'][0]['snippet']['description']
        self.__url = f'https://www.youtube.com/channel/{self.__channel_id}'



