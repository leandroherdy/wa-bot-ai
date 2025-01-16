import requests


class Waha:
    def __init__(self):
        self.__api_url = "http://waha:3000"

    def send_message(self, chat_id, media_url, message):
        url = f"{self.__api_url}/api/sendText"
        headers = {"Content-Type": "application/json"}

        payload = {
            "session": "default",
            "chatId": chat_id,
            "media": media_url,
            "text": message,
        }
        requests.post(
            url=url,
            json=payload,
            headers=headers,
        )

    def start_typing(self, chat_id):
        url = f"{self.__api_url}/api/startTyping"
        headers = {
            "content-Type": "application/json",
        }
        payload = {
            "session": "default",
            "chatId": chat_id,
        }
        requests.post(
            url=url,
            json=payload,
            headers=headers,
        )

    def stop_typing(self, chat_id):
        url = f"{self.__api_url}/stopTyping"
        headers = {
            "content-Type": "application/json",
        }
        payload = {
            "session": "default",
            "chatId": chat_id,
        }
        requests.post(
            url=url,
            json=payload,
            headers=headers,
        )
