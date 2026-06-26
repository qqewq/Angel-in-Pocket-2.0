class AccountingLedger:
    def __init__(self, db):
        self.db = db

    async def record_transaction(self, description: str, debit_account: str, credit_account: str, amount: float):
        entry = {
            "description": description,
            "debit": debit_account,
            "credit": credit_account,
            "amount": amount,
        }
        await self.db.insert("ledger", entry)

    async def get_balance(self, account: str) -> float:
        return await self.db.sum("ledger", account)
