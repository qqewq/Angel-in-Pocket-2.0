import sys
sys.path.append("./gra_core")  # Assume submodule or installed package
from gra_core import StabilityEngine

class GRAStabilityClient:
    def __init__(self, gra_core_path: str = None):
        self.engine = StabilityEngine()

    async def evaluate_scenario(self, scenario: dict) -> dict:
        stability = self.engine.evaluate(scenario)
        return {"score": stability.score, "contradictions": stability.contradictions}

    async def rank_strategies(self, scenarios: list[dict]) -> list[dict]:
        ranked = self.engine.rank(scenarios)
        return [{"id": r.id, "score": r.score, "plan": r.plan} for r in ranked]

    async def nullify_branch(self, branch_id: str):
        self.engine.nullify(branch_id)
