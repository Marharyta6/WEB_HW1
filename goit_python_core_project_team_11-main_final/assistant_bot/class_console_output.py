from abc import ABC
from enum import Enum, auto


class Terminals(Enum):
    TERMINAL = auto()
    TELEGRAM = auto()
    VIBER = auto()


class ConsoleOutputAbstract(ABC):
    service: Enum

    def output(self, text: str, *args) -> str:
        ...


class TerminalOutput(ConsoleOutputAbstract):
    service = Terminals.TERMINAL

    def output(self, text: str, *args) -> None:
        text = self.get_clear_text(text)
        print(f"Send to TerminalOutput: {text}")




class Telegram:
    def __init__(self, token):
        self.token = token

    def send_message(self, text):
        print(f"Send {text} to Telegram")


class TelegramOutput(ConsoleOutputAbstract):
    service = Terminals.TELEGRAM

    def __init__(self, token) -> None:
        self.telegram_client = Telegram(token)
        super().__init__()



class Viber:
    def __init__(self, token):
        self.token = token

    def send_message(self, text):
        print(f"Send {text} to Viber")


class ViberOutput(ConsoleOutputAbstract):
    service = Terminals.VIBER

    def __init__(self, token) -> None:
        self.viber_client = Viber(token)
        super().__init__()
