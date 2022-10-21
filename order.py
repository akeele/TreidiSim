from dataclasses import dataclass
from typing import Literal
from asset import Asset

@dataclass
class Order:
    """
    Represents order.
    """
    asset: Asset
    quantity: int
    direction: Literal["BUY", "SELL"]
