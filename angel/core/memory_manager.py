from tools.database import Database

class MemoryManager:
    def __init__(self, db: Database):
        self.db = db

    async def retrieve(self, domain: str, query: dict) -> list:
        return await self.db.fetch_memories(domain, query)

    async def store(self, domain: str, entry: dict):
        await self.db.insert_memory(domain, entry)

    async def forget_branch(self, branch_id: str):
        await self.db.delete_memory(branch_id)
