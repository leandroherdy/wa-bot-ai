import requests
import logging


class Waha:
    def __init__(self):
        self.__api_url = "http://waha:3000"
        self.__headers = {"Content-Type": "application/json"}
        self.__logger = logging.getLogger(__name__)

    def send_message(self, chat_id: str, message: str):
        """
        Send a text message to a specific chat.

        Args:
            chat_id (str): The ID of the chat to send the message to.
            message (str): The text message to send.
        """
        url = f"{self.__api_url}/api/sendText"
        payload = {
            "session": "default",
            "chatId": chat_id,
            "text": message,
        }
        try:
            response = requests.post(url=url, json=payload, headers=self.__headers)
            response.raise_for_status()
            self.__logger.info(f"Message sent to chat_id: {chat_id}")
        except requests.exceptions.HTTPError as http_err:
            self.__logger.error(
                f"HTTP error occurred while sending message: {http_err}"
            )
        except requests.exceptions.RequestException as req_err:
            self.__logger.error(
                f"Request error occurred while sending message: {req_err}"
            )
        except Exception as err:
            self.__logger.error(
                f"Unexpected error occurred while sending message: {err}"
            )
            raise

    def start_typing(self, chat_id: str):
        """
        Simulate typing in a chat.

        Args:
            chat_id (str): The ID of the chat where typing is simulated.
        """
        url = f"{self.__api_url}/api/startTyping"
        payload = {
            "session": "default",
            "chatId": chat_id,
        }
        try:
            response = requests.post(url=url, json=payload, headers=self.__headers)
            response.raise_for_status()
            self.__logger.info(f"Typing simulation started for chat_id: {chat_id}")
        except requests.exceptions.HTTPError as http_err:
            self.__logger.error(
                f"HTTP error occurred while starting typing: {http_err}"
            )
        except requests.exceptions.RequestException as req_err:
            self.__logger.error(
                f"Request error occurred while starting typing: {req_err}"
            )
        except Exception as err:
            self.__logger.error(
                f"Unexpected error occurred while starting typing: {err}"
            )
            raise

    def stop_typing(self, chat_id: str):
        """
        Stop the typing simulation in a chat.

        Args:
            chat_id (str): The ID of the chat where typing simulation is stopped.
        """
        url = f"{self.__api_url}/api/stopTyping"
        payload = {
            "session": "default",
            "chatId": chat_id,
        }
        try:
            response = requests.post(url=url, json=payload, headers=self.__headers)
            response.raise_for_status()
            self.__logger.info(f"Typing simulation stopped for chat_id: {chat_id}")
        except requests.exceptions.HTTPError as http_err:
            self.__logger.error(
                f"HTTP error occurred while stopping typing: {http_err}"
            )
        except requests.exceptions.RequestException as req_err:
            self.__logger.error(
                f"Request error occurred while stopping typing: {req_err}"
            )
        except Exception as err:
            self.__logger.error(
                f"Unexpected error occurred while stopping typing: {err}"
            )
            raise
