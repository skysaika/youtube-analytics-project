import datetime
import os
import isodate
from dotenv import load_dotenv

from googleapiclient.discovery import build
from settings import ENV_FILE

load_dotenv(ENV_FILE)


class YouTube:
    """Класс для ютуб-канала"""
    __api_key: str = os.getenv('API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__api_key)

    @classmethod
    def get_channel(cls, channel_id):
        """Класс метод получает каналы"""
        return cls.__youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    @classmethod
    def get_video(cls, video_id):
        """Класс метод получает список видео"""
        return cls.__youtube.videos().list(
            part='snippet,statistics,contentDetails,topicDetails',
            id=video_id
        ).execute()

    @classmethod
    def get_playlist(cls, playlist_id):
        """Класс метод получает плейлисты"""
        return cls.__youtube.playlists().list(
            id=playlist_id,
            part='contentDetails, snippet',
            maxResults=50,
        ).execute()

    @classmethod
    def get_playlist_video_ids(cls, playlist_id):
        """Класс метод получает все id определенного плейлиста"""
        ids = []
        playlist = cls.__youtube.playlistItems().list(
            playlistId=playlist_id,
            part='contentDetails',
            maxResults=50,
        ).execute()
        for video in playlist['items']:
            ids.append(video['contentDetails']['videoId'])
        return ids

    @classmethod
    def get_videos_duration(cls, playlist_id) -> datetime.timedelta:
        """Класс метод описание всех видео"""
        video_response = cls.__youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(cls.get_playlist_video_ids(playlist_id))
        ).execute()
        delta = datetime.timedelta()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            delta += duration
        return delta

    @classmethod
    def get_videos_in_playlist(cls, playlist_id):
        """Класс метод получает видео в плейлисте"""
        video_response = cls.__youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(cls.get_playlist_video_ids(playlist_id))
        ).execute()
        return video_response['items']
