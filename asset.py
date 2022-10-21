from dataclasses import dataclass

@dataclass
class Asset:

    sid: int
    ticker: str
    currency: str
