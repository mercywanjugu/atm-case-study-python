class Screen:
    def display_message(self, message: str) -> None:
        print(message, end="")

    def display_message_line(self, message: str) -> None:
        print(message)

    def display_dollar_amount(self, amount: float) -> None:
        print(f"${amount:,.2f}")
