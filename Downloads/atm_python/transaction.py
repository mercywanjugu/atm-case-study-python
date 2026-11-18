from abc import ABC, abstractmethod


class Transaction(ABC):
    def __init__(self, user_account_number: int, atm_screen, atm_bank_database) -> None:
        self._account_number = user_account_number
        self._screen = atm_screen
        self._bank_database = atm_bank_database

    def get_account_number(self) -> int:
        return self._account_number

    def get_screen(self):
        return self._screen

    def get_bank_database(self):
        return self._bank_database

    @abstractmethod
    def execute(self) -> None:
        pass
