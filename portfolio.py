from dataclasses import dataclass
from asset import Asset
from position import Position
from typing import Dict

@dataclass
class Portfolio:
    """
    Portfolio contains assets
    """
    assets: Dict[Asset, Position]
    cash: float

    def get_position(self, asset):
        return self.assets[asset]

    def update_position(self, asset, position):
        self.assets[asset] = position

    def reduce_cash(self, amount):
        self.cash -= amount

    def add_cash(self, amount):
        self.cash += amount

    @property
    def total_value(self):
        value = 0
        for asset, position in self.assets.items():
            value += position.quantity * position.price

        return value + self.cash
