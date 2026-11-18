class Account:
    def __init__(self, account_number: int, pin: int, available_balance: float, total_balance: float) -> None:
        self._account_number = account_number
        self._pin = pin
        self._available_balance = available_balance
        self._total_balance = total_balance

    def validate_pin(self, user_pin: int) -> bool:
        return user_pin == self._pin

    def get_available_balance(self) -> float:
        return self._available_balance

    def get_total_balance(self) -> float:
        return self._total_balance

    def credit(self, amount: float) -> None:
        self._total_balance += amount

    def debit(self, amount: float) -> None:
        self._available_balance -= amount
        self._total_balance -= amount

    def get_account_number(self) -> int:
        return self._account_number
