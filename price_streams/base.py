from bar_streamer import HistoricBarStreamer
from data.historical import HistoricBars


class PriceStream:
    """
    Interface for different kinds of price streams
    """
    def stream_next(self):
        raise NotImplementedError


def initialiaze_price_stream(config):
    """
    Finds and initializes the correct class.
    """
    if config["price_stream"] == "historical_bars":
        bars = HistoricBars(config.assets).get(config.start_date, config.end_date)
        return HistoricBarStreamer(bars)
