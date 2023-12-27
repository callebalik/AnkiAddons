from typing import List, NamedTuple
import datetime
import math

from aqt import mw


MONTHS = (
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
)


class InvalidDateLikeStringError(Exception):
    def __init__(self, date_string: str) -> None:
        self.date_string = date_string
        super().__init__()


class InvalidDateStringError(InvalidDateLikeStringError):
    """Date string is invalid."""

    def __str__(self) -> str:
        return (
            f'Invalid date: "{self.date_string}"\n'
            'Dates should be formatted like: "Jan 3 2021"'
        )


class InvalidDateRangeError(InvalidDateLikeStringError):
    """Date range string is invalid"""

    def __str__(self) -> str:
        return (
            f'Invalid date range: "{self.date_string}"\n'
            'Date ranges should be formatted like "Aug 3 2021 - Aug 15 2021"'
        )


class Goal(NamedTuple):
    """Raw goal item stored in config."""

    name: str
    query: str
    due: str
    days_per_week: int
    excluded_dates: str
    show_on_main: bool


def get_study_days(goal: Goal) -> int:
    """Get number of valid study days until due.

    Can raise InvalidDateStringError.
    """
    # TODO: handle due is earlier than today
    due = parse_date(goal.due)
    study_days = (due - datetime.date.today()).days + 1
    study_days = math.floor(study_days / 7 * goal.days_per_week)
    if goal.excluded_dates:
        excluded = parse_excluded_dates(goal.excluded_dates)
        study_days -= len(excluded)

    return study_days


def parse_date(date_string: str) -> datetime.date:
    """Parse string that contain a single date.
    Accepted format:
        - year: 32 - 9999
        - month: 3 digit string of full name
        - date: 1 or 2 digit integer

    Can raise InvalidDateStringError
    """
    date_string = date_string.strip()
    date_nodes = [s.strip() for s in date_string.split()]
    try:
        assert len(date_nodes) == 3
        date = {"year": -1, "month": -1, "day": -1}
        for node in date_nodes:
            try:
                val = int(node)
                if val < 32:
                    date["day"] = val
                else:
                    date["year"] = val
            except:
                val = MONTHS.index(node.lower()) + 1
                date["month"] = val
        return datetime.date(**date)
    except:
        raise InvalidDateStringError(date_string)


def parse_date_range(date_range: str) -> List[datetime.date]:
    """Parse string of a single date range. Return list of datetime including start and end.

    eg. "Jun 16 2021 - Jun 28 2021"
    Can raise InvalidDateRangeError
    """
    date_range = date_range.strip()
    date_strings = date_range.split("-")
    if len(date_strings) != 2:
        raise InvalidDateRangeError(date_range)
    start_date = parse_date(date_strings[0])
    end_date = parse_date(date_strings[1])
    if end_date < start_date:
        raise InvalidDateRangeError(date_range)

    dates: List[datetime.date] = []
    current = start_date
    step = datetime.timedelta(days=1)
    while current <= end_date:
        dates.append(current)
        current += step
    return dates


def parse_excluded_dates(dates_string: str) -> List[datetime.date]:
    """Parse date or date range strings, or empty "".

    eg. "Jun 16 2021 - Jul 2 2021, Aug 3 2021"

    Can raise InvalidDateRangeError and InvalidDateStringError.
    """
    if not dates_string.strip():
        return []

    dates_and_ranges = dates_string.strip().split(",")
    dates: List[datetime.date] = []
    for date_string in dates_and_ranges:
        if "-" in date_string:
            ds = parse_date_range(date_string)
            dates.extend(ds)
        else:
            d = parse_date(date_string)
            dates.append(d)

    valid_dates: List[datetime.date] = []
    for date in dates:
        if date >= datetime.date.today():
            valid_dates.append(date)
    return valid_dates


def get_new_cards_count(query: str) -> int:
    return get_cards_count(f"is:new {query}")


def get_cards_count(query: str) -> int:
    cards = mw.col.find_cards(query, order=False)
    return len(cards)


def d_minus_until(due: str) -> int:
    """May return negative number if due date has passed."""
    diff = parse_date(due) - datetime.date.today()
    return diff.days
