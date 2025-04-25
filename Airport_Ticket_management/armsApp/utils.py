class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ConfigManager(Singleton):
    def __init__(self):
        if not hasattr(self, 'settings'):
            self.settings = {}

    def get_setting(self, key):
        return self.settings.get(key, None)

    def set_setting(self, key, value):
        self.settings[key] = value


class CreditPayment:
    def process(self, amount):
        return f"Processed credit payment of {amount}"


class PayPalPayment:
    def process(self, amount):
        return f"Processed PayPal payment of {amount}"


class PaymentFacade:
    @staticmethod
    def process_payment(amount, method):
        if method == 'credit':
            return CreditPayment().process(amount)
        elif method == 'paypal':
            return PayPalPayment().process(amount)
        return "Invalid payment method"


class RegularPricing:
    def get_price(self, base_price):
        return base_price


class PremiumPricing:
    def get_price(self, base_price):
        return base_price * 0.8


class PricingContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def get_final_price(self, base_price):
        return self.strategy.get_price(base_price)
