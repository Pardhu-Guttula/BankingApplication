# Epic Title: Persist shopping cart state in PostgreSQL

from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    description: str
    available: bool