import logging

LOG = logging.getLogger(__name__)

class TradingSystem:
    """Defines the whole trading system"""

    def __init__(self, price_stream, strategy, portfolio_handler, broker):
        self.price_stream = price_stream
        self.strategy = strategy
        self.portfolio_handler = portfolio_handler
        self.broker = broker
        self.history = []

    def run(self):
        """
        Start point for the trading or backtesting session.
        """
        LOG.info("Start session.")
        while True:
            try:
                price = next(self.price_stream)
            except StopIteration:
                LOG.info("Trading stopped. No more prices.")
                break

            signal = self.strategy.get_signal(price)
            order = self.portfolio_handler.generate_order(signal)
            self.broker.execute_order(order)

            portfolio = self.broker.get_portfolio()
            self.history.append(portfolio)

        LOG.info("End session")
        return self.history
