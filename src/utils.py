import json


def print_info(self) -> None:
    """Выводит в консоль информацию о канале."""
    channel = self.__youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
    print(json.dumps(channel, indent=2, ensure_ascii=False))

