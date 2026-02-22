# Epic Title: Sort Products by Price

from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    description: str