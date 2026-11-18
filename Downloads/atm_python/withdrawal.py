from transaction import Transaction


class Withdrawal(Transaction):
    CANCELED = 6

    def __init__(self, user_account_number: int, atm_screen, atm_bank_database, atm_keypad, atm_cash_dispenser) -> None:
        super().__init__(user_account_number, atm_screen, atm_bank_database)
        self._keypad = atm_keypad
        self._cash_dispenser = atm_cash_dispenser

    def execute(self) -> None:
        cash_dispensed = False
        bank_database = self.get_bank_database()
        screen = self.get_screen()

        while not cash_dispensed:
            amount = self._display_menu_of_amounts()
            if amount != self.CANCELED:
                available_balance = bank_database.get_available_balance(self.get_account_number())
                if amount <= available_balance:
                    if self._cash_dispenser.is_sufficient_cash_available(amount):
                        bank_database.debit(self.get_account_number(), amount)
                        self._cash_dispenser.dispense_cash(amount)
                        cash_dispensed = True
                        screen.display_message_line("\nYour cash has been dispensed. Please take it now.")
                    else:
                        screen.display_message_line("\nInsufficient cash available in the ATM machine.")
                else:
                    screen.display_message_line("\nInsufficient funds in your account.")
            else:
                screen.display_message_line("\nCanceling transaction...")
                return

    def _display_menu_of_amounts(self) -> int:
        user_choice = 0
        screen = self.get_screen()
        amounts = [0, 20, 40, 60, 100, 200]

        while user_choice == 0:
            screen.display_message_line("\nWithdrawal Menu:")
            screen.display_message_line("1 - $20      2 - $40      3 - $60")
            screen.display_message_line("4 - $100     5 - $200     6 - Cancel transaction")
            screen.display_message("\nChoose a withdrawal amount: ")

            choice = self._keypad.get_input()
            if 1 <= choice <= 5:
                user_choice = amounts[choice]
            elif choice == self.CANCELED:
                user_choice = self.CANCELED
            else:
                screen.display_message_line("\nInvalid choice. Try again.")

        return user_choice
