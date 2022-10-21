import logging
from ..broker import BrokerInterface
from ..asset import Asset
from ..position import Position

LOG = logging.getLogger(__name__)

class SimulatedBroker(BrokerInterface):
    """
    Simulated broker for backtesting.
    """
    def __init__(self, portfolio, price_stream):
        self.portfolio = portfolio
        self.price_stream = price_stream

    def _get_current_price(self, asset: Asset):
        return self.price_stream.peek_future(asset)

    def get_portfolio(self):
        return self.portfolio

    def execute_order(self, order):
        """
        Executes the order.
        """
        LOG.info("Executing order %s", order)
        current_price = self._get_current_price(order.asset)
        current_position = self.portfolio.get_position(order.asset)

        if order.direction == "BUY":
            new_quantity = current_position.quantity + order.quantity
            self.portfolio.reduce_cash(current_price * order.quantity)

        elif order.direction == "SELL":
            new_quantity = current_position.quantity - order.quantity
            self.portfolio.add_cash(current_price * order.quantity)
        else:
            LOG.error("Order must be BUY or SELL")
            return

        position = Position(quantity=new_quantity, price=current_price)
        self.portfolio.update_position(order.asset, position)
