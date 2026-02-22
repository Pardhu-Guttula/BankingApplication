# Epic Title: Monitor user behavior metrics

from dataclasses import dataclass
import datetime

@dataclass
class UserSession:
    session_id: int
    user_id: int
    start_time: datetime.datetime
    end_time: datetime.datetime

@dataclass
class PageView:
    view_id: int
    user_id: int
    page_url: str
    timestamp: datetime.datetime

@dataclass
class ClickThroughRate:
    click_id: int
    user_id: int
    element_id: str
    timestamp: datetime.datetime
    clicked: bool