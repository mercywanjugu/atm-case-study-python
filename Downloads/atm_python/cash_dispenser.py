class CashDispenser:
    INITIAL_COUNT = 500

    def __init__(self) -> None:
        self._count = self.INITIAL_COUNT

    def dispense_cash(self, amount: int) -> None:
        bills_required = amount // 20
        self._count -= bills_required

    def is_sufficient_cash_available(self, amount: int) -> bool:
        bills_required = amount // 20
        return self._count >= bills_required
