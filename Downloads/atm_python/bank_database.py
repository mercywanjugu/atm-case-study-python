from account import Account


class BankDatabase:
    def __init__(self) -> None:
        self._accounts = [
            Account(12345, 54321, 1000.0, 1200.0),
            Account(98765, 56789, 200.0, 200.0)
        ]

    def _get_account(self, account_number: int):
        for current_account in self._accounts:
            if current_account.get_account_number() == account_number:
                return current_account
        return None

    def authenticate_user(self, user_account_number: int, user_pin: int) -> bool:
        user_account = self._get_account(user_account_number)
        if user_account is not None:
            return user_account.validate_pin(user_pin)
        return False

    def get_available_balance(self, account_number: int) -> float:
        return self._get_account(account_number).get_available_balance()

    def get_total_balance(self, account_number: int) -> float:
        return self._get_account(account_number).get_total_balance()

    def credit(self, account_number: int, amount: float) -> None:
        self._get_account(account_number).credit(amount)

    def debit(self, account_number: int, amount: float) -> None:
        self._get_account(account_number).debit(amount)
