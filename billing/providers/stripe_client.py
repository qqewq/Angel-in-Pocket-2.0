import stripe

class StripeClient:
    def __init__(self, api_key: str):
        stripe.api_key = api_key

    async def create_checkout_session(self, user_id: str, plan: dict) -> str:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{'price': plan['stripe_price_id'], 'quantity': 1}],
            mode='subscription',
            success_url='https://angel.ai/success',
            cancel_url='https://angel.ai/cancel',
            client_reference_id=user_id,
        )
        return session.url

    async def apply_coupon(self, user_id: str, coupon: str):
        # Simplified: apply to next invoice
        pass
