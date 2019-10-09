class PriceBarStreamer:
    
    def __init__(self, price_bars):
        self.price_bars = price_bars
        self.continue_backtest = True

    def _iterate_prices(self):
        return self.price_bars.iterrows()

    def stream_next(self):
        try:
            index, current_bar = next(self._iterate_prices())
        except StopIteration:
            self.continue_backtest = False
            return

        
