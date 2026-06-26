from business.arbitrage.strategies import ArbitrageStrategies
from business.arbitrage.data_feeds import DataFeeds
from gra_integration.client import GRAStabilityClient

class ArbitrageAgent:
    def __init__(self, config):
        self.feeds = DataFeeds(config.exchange_apis)
        self.strategies = ArbitrageStrategies()
        self.gra = GRAStabilityClient(config.gra_core_path)

    async def find_opportunities(self, pair: str = "BTC/USDT") -> list:
        prices = await self.feeds.fetch_prices(pair)
        raw_opportunities = self.strategies.generate(prices)
        # Use GRA to rank by stability
        ranked = await self.gra.rank_strategies(raw_opportunities)
        return [opp for opp in ranked if opp["score"] > 0.7]

    async def execute_arbitrage(self, opportunity: dict) -> dict:
        # Execute trade across exchanges (mock)
        return {"status": "executed", "profit": opportunity["expected_profit"]}
