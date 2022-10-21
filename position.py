from dataclasses import dataclass

@dataclass
class Position:
    """
    Represents position in an asset.
    """
    quantity: int
    price: float
