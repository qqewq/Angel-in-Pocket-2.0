from billing.providers.stripe_client import StripeClient
from billing.providers.paypal_client import PayPalClient
from billing.providers.crypto_client import CryptoClient
from billing.tariff_manager import TariffManager

class SubscriptionManager:
    def __init__(self, config):
        self.stripe = StripeClient(config.stripe_api_key)
        self.paypal = PayPalClient(config.paypal_client_id, config.paypal_secret)
        self.crypto = CryptoClient(config.crypto_wallet)
        self.tariffs = TariffManager(config.tariff_plans)

    async def create_subscription(self, user_id: str, plan_id: str, payment_method: str):
        plan = self.tariffs.get(plan_id)
        if payment_method == "stripe":
            return await self.stripe.create_checkout_session(user_id, plan)
        elif payment_method == "paypal":
            return await self.paypal.create_billing_agreement(user_id, plan)
        elif payment_method == "crypto":
            return await self.crypto.generate_invoice(user_id, plan)
        raise ValueError(f"Unknown payment method: {payment_method}")

    def calculate_mrr(self, active_subs: list) -> float:
        return sum(sub["amount"] for sub in active_subs if sub["status"] == "active")

    async def handle_churn_risk(self, user_id: str, angel_core):
        # Let angel decide retention action based on GRA stability
        context = {"user_id": user_id, "churn_probability": 0.75}
        decision = await angel_core.decide("billing_churn", context)
        if decision.get("action") == "offer_discount":
            await self.stripe.apply_coupon(user_id, "RETENTION10")
