from enum import Enum

EventType = Enum("EventType", "BAR")

class Event:
    """Base class for all events"""
    def __init__(self, asset):
        self.ticker = asset.ticker

class BarEvent(Event):

    def __init__(self, time, open_price, high_price, low_price, close_price, volume):

        super().__init__()
        self.type = EventType.BAR
        self.time = time
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.volume = volume

