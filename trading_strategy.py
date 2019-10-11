from abc import ABC, abstractmethod


class TradingStrategy(ABC):


    def __init__(self, assets):
        self.assets = assets
    
    @abstractmethod
    def calculate_signals(self):

        raise NotImplementedError("Should implement calculate_signals() method")
