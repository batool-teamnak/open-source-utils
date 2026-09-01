"""Small date and timezone helpers with no third-party dependencies."""

from calendar import monthrange
from datetime import date, datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo


def date_range(start, end):
    """Yield ISO dates from *start* through *end*, inclusive.

    ``start`` and ``end`` may be ``date`` objects or ``YYYY-MM-DD`` strings.
    Raises ``ValueError`` when the end precedes the start.
    """
    first = date.fromisoformat(start) if isinstance(start, str) else start
    last = date.fromisoformat(end) if isinstance(end, str) else end
    if not isinstance(first, date) or not isinstance(last, date):
        raise TypeError("start and end must be date objects or YYYY-MM-DD strings")
    if last < first:
        raise ValueError("end must be on or after start")

    current = first
    while current <= last:
        yield current.isoformat()
        current += timedelta(days=1)


def month_dates(year, month):
    """Yield every ISO date in a calendar month, including leap days."""
    last_day = monthrange(year, month)[1]
    return date_range(date(year, month, 1), date(year, month, last_day))


def convert_timezone(value, target_timezone):
    """Convert an aware datetime to ``target_timezone``.

    Naive datetimes are rejected so their timezone is never guessed.
    """
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("value must be a timezone-aware datetime")
    return value.astimezone(ZoneInfo(target_timezone))


def start_of_day(value, target_timezone="UTC"):
    """Return midnight at ``value``'s calendar date in the requested zone."""
    zone = ZoneInfo(target_timezone)
    day = value.astimezone(zone).date() if value.tzinfo is not None else value.date()
    return datetime.combine(day, time.min, tzinfo=zone)


def to_utc(value):
    """Convert a timezone-aware datetime to UTC."""
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("value must be a timezone-aware datetime")
    return value.astimezone(timezone.utc)
