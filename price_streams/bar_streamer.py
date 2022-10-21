from base import PriceStream

class HistoricBarStreamer(PriceStream):
    """
    Streams historical bars.
    """
    def __init__(self, bars):
        self.bars = bars

    def _iterate_prices(self):
        return self.bars.iterrows()

    def stream_next(self):
        try:
            index, current_bar = next(self._iterate_prices())
        except StopIteration:
            return
