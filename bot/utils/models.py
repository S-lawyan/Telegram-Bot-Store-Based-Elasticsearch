from dataclasses import dataclass
import json


@dataclass(kw_only=True)
class Product:
    def __init__(self):
        self.product_name: str = ''
        self.price: float = 0
        self.quantity: int | None = 0
        self.article: int = 0
        self.trader_id: int = 0
