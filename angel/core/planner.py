class Planner:
    def __init__(self, llm_provider):
        self.llm = llm_provider

    async def generate_scenarios(self, domain: str, context: dict, memories: list) -> list[dict]:
        prompt = f"Generate 3 action scenarios for domain '{domain}' given context: {context} and memories: {memories}"
        response = await self.llm.complete(prompt)
        return self._parse_scenarios(response)

    def _parse_scenarios(self, raw: str) -> list[dict]:
        return [{"id": f"s{i}", "plan": raw}]  # Simplified
