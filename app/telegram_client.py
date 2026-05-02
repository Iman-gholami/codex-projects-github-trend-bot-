import logging

import requests

logger = logging.getLogger(__name__)


class TelegramClient:
    def __init__(self, bot_token: str, channel_id: str) -> None:
        self.bot_token = bot_token
        self.channel_id = channel_id
        self.url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    def send_message(self, text: str) -> None:
        payload = {
            "chat_id": self.channel_id,
            "text": text,
            "disable_web_page_preview": False,
        }
        response = requests.post(self.url, json=payload, timeout=20)
        response.raise_for_status()
        logger.info("Sent message to Telegram channel")
