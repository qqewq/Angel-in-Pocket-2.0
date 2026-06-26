from __future__ import annotations
import asyncio
from angel.core.planner import Planner
from angel.core.memory_manager import MemoryManager
from gra_integration.client import GRAStabilityClient
from tools.llm_provider import LLMProvider

class AngelCore:
    """Central decision-making agent."""
    def __init__(self, config):
        self.llm = LLMProvider(config.llm_model)
        self.planner = Planner(self.llm)
        self.memory = MemoryManager(config.memory_backend)
        self.gra = GRAStabilityClient(config.gra_core_path)

    async def decide(self, domain: str, context: dict) -> dict:
        # Retrieve relevant memories
        memories = await self.memory.retrieve(domain, context)
        # Generate candidate scenarios
        scenarios = await self.planner.generate_scenarios(domain, context, memories)
        # Stability evaluation with GRA
        ranked = await self.gra.rank_strategies(scenarios)
        best = ranked[0]
        # Log decision and update memory
        await self.memory.store(domain, {"context": context, "decision": best})
        return best

    async def nullify_unstable_branch(self, branch_id: str):
        await self.gra.nullify_branch(branch_id)
        await self.memory.forget_branch(branch_id)
