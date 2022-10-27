import os
from typing import List

from django.core.management.base import CommandError
from django.utils.timezone import datetime

from demo.models import Record


def parse_datetime(value: str, line: int = None) -> datetime:
    format_str = "%Y%m%d%H%M%S"
    try:
        return datetime.strptime(value, format_str)
    except ValueError:
        raise CommandError(
            "Date time data '{}' (in line {}) does not match format '{}'".format(
                value, line, format_str
            )
        )


def extract_values(path: str) -> List[dict]:
    data: List[dict] = []
    with open(path, "r") as file:
        file.readline()
        for index, line in enumerate(file.readlines()):
            line_number = index + 2
            parts = line.split(",")
            try:
                data.append(
                    {
                        "nmi": parts[1],
                        "meter_serial_number": parts[6],
                        "read": parts[13],
                        "date": parse_datetime(parts[14], line_number),
                        "file_name": os.path.basename(path),
                    }
                )
            except IndexError:
                raise CommandError(
                    "There is error while extracting data from CSV (line {})".format(
                        line_number
                    )
                )
    return data


def create_record_from_values(data) -> Record:
    record = Record(**data)
    record.save()
    return record
