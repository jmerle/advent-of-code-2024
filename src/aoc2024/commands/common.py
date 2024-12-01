import os
from pathlib import Path

from dotenv import load_dotenv
from requests import Session

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
DAYS_ROOT = PROJECT_ROOT / "src" / "aoc2024" / "days"


def get_requests_session() -> Session:
    session = Session()
    session.headers.update({"User-Agent": "https://github.com/jmerle/advent-of-code-2024 by jaspervmerle@gmail.com"})

    load_dotenv()
    session.cookies.set("session", os.environ["SESSION_COOKIE"])

    return session


def get_day_directory(day: int) -> Path:
    return DAYS_ROOT / f"day{day:02}"
