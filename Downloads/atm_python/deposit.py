from transaction import Transaction


class Deposit(Transaction):
    CANCELED = 0

    def __init__(self, user_account_number: int, atm_screen, atm_bank_database, atm_keypad, atm_deposit_slot) -> None:
        super().__init__(user_account_number, atm_screen, atm_bank_database)
        self._keypad = atm_keypad
        self._deposit_slot = atm_deposit_slot

    def execute(self) -> None:
        bank_database = self.get_bank_database()
        screen = self.get_screen()

        amount = self._prompt_for_deposit_amount()
        if amount != self.CANCELED:
            screen.display_message("\nPlease insert a deposit envelope containing ")
            screen.display_dollar_amount(amount)
            screen.display_message_line(" in the deposit slot.")

            if self._deposit_slot.is_envelope_received():
                screen.display_message_line("\nYour envelope has been received.")
                screen.display_message_line("NOTE: The money deposited will not be available until we verify the amount.")
                bank_database.credit(self.get_account_number(), amount)
            else:
                screen.display_message_line("\nYou did not insert an envelope, so the ATM has canceled your transaction.")
        else:
            screen.display_message_line("\nCanceling transaction...")

    def _prompt_for_deposit_amount(self) -> float:
        screen = self.get_screen()
        screen.display_message("\nPlease enter a deposit amount in CENTS (or 0 to cancel): ")
        cents = self._keypad.get_input()
        if cents == self.CANCELED:
            return self.CANCELED
        return cents / 100.0
