# Epic Title: Add products to the shopping cart

from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    description: str
    available: bool