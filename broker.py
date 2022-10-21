from asset import Asset

class BrokerInterface:
    """
    Interface for brokers.
    """
    def _get_current_price(self, asset: Asset):
        raise NotImplementedError

    def get_portfolio(self):
        raise NotImplementedError

    def execute_order(self, order):
        raise NotImplementedError
