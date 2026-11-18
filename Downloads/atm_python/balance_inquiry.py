from transaction import Transaction


class BalanceInquiry(Transaction):
    def execute(self) -> None:
        bank_database = self.get_bank_database()
        screen = self.get_screen()

        available_balance = bank_database.get_available_balance(self.get_account_number())
        total_balance = bank_database.get_total_balance(self.get_account_number())

        screen.display_message_line("\nBalance Information:")
        screen.display_message(" - Available balance: ")
        screen.display_dollar_amount(available_balance)
        screen.display_message(" - Total balance:     ")
        screen.display_dollar_amount(total_balance)
        screen.display_message_line("")
