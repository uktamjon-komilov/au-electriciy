from django.utils.timezone import datetime


def parse_datetime(value: str) -> datetime:
    return datetime.strptime(value, "%Y%m%d%H%M%S")