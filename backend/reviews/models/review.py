# Epic Title: Display reviews on product detail pages

from dataclasses import dataclass
import datetime

@dataclass
class Review:
    review_id: int
    product_id: int
    user_id: int
    rating: int
    title: str
    review_text: str
    moderated: bool
    created_at: datetime.datetime