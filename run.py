import os
import yaml
from price_streams.base import initialize_price_stream
from strategies.base import initialize_strategy
from portfolio_handler import initialize_portfolio_handler
from brokers.base import initialiaze_broker
from stats import save_stats
from plots import plot_curves


def read_config(config_file: str) -> dict:
    with open(config_file, 'r') as f:
        config: dict = yaml.safe_load(f)
    return config

def initialize_price_stream(config):
    match config.stream_type:
        case "historical_bars":
            return HistoricBarStreamer(config)


def main() -> None:
    """
    Starting point.
    """
    config = read_config(os.environ["TRADING_CONFIG"])

    price_stream = initialize_price_stream(config)
    strategy = initialize_strategy(config)
    portfolio_handler = initialize_portfolio_handler(config)
    broker = initialiaze_broker(config)

    trading_system = TradingSystem(
        price_stream,
        strategy,
        portfolio_handler,
        broker
    )

    history = trading_system.run()

    save_stats(history)
    plot_curves(history)

if __name__ == "__main__":
    main()
