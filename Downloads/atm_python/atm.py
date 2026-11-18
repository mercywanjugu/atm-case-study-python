from screen import Screen
from keypad import Keypad
from cash_dispenser import CashDispenser
from deposit_slot import DepositSlot
from bank_database import BankDatabase
from balance_inquiry import BalanceInquiry
from withdrawal import Withdrawal
from deposit import Deposit


class ATM:
    BALANCE_INQUIRY = 1
    WITHDRAWAL = 2
    DEPOSIT = 3
    EXIT = 4

    def __init__(self) -> None:
        self._user_authenticated = False
        self._current_account_number = 0
        self._screen = Screen()
        self._keypad = Keypad()
        self._cash_dispenser = CashDispenser()
        self._deposit_slot = DepositSlot()
        self._bank_database = BankDatabase()

    def run(self) -> None:
        while True:
            while not self._user_authenticated:
                self._screen.display_message_line("\nWelcome!")
                self._authenticate_user()

            self._perform_transactions()
            self._user_authenticated = False
            self._current_account_number = 0
            self._screen.display_message_line("\nThank you! Goodbye!")

    def _authenticate_user(self) -> None:
        self._screen.display_message("\nPlease enter your account number: ")
        account_number = self._keypad.get_input()
        self._screen.display_message("Enter your PIN: ")
        pin = self._keypad.get_input()

        self._user_authenticated = self._bank_database.authenticate_user(account_number, pin)
        if self._user_authenticated:
            self._current_account_number = account_number
        else:
            self._screen.display_message_line("Invalid account number or PIN. Please try again.")

    def _perform_transactions(self) -> None:
        user_exited = False

        while not user_exited:
            main_menu_selection = self._display_main_menu()

            if main_menu_selection in (self.BALANCE_INQUIRY, self.WITHDRAWAL, self.DEPOSIT):
                current_transaction = self._create_transaction(main_menu_selection)
                current_transaction.execute()
            elif main_menu_selection == self.EXIT:
                self._screen.display_message_line("\nExiting the system...")
                user_exited = True
            else:
                self._screen.display_message_line("\nYou did not enter a valid selection. Try again.")

    def _display_main_menu(self) -> int:
        self._screen.display_message_line("\nMain Menu:")
        self._screen.display_message_line("1 - View my balance")
        self._screen.display_message_line("2 - Withdraw cash")
        self._screen.display_message_line("3 - Deposit funds")
        self._screen.display_message_line("4 - Exit\n")
        self._screen.display_message("Enter a choice: ")
        return self._keypad.get_input()

    def _create_transaction(self, transaction_type: int):
        if transaction_type == self.BALANCE_INQUIRY:
            return BalanceInquiry(self._current_account_number, self._screen, self._bank_database)
        elif transaction_type == self.WITHDRAWAL:
            return Withdrawal(self._current_account_number, self._screen, self._bank_database, self._keypad, self._cash_dispenser)
        elif transaction_type == self.DEPOSIT:
            return Deposit(self._current_account_number, self._screen, self._bank_database, self._keypad, self._deposit_slot)
        return None
