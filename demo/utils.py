from django.utils.timezone import datetime
from typing import List
from django.core.management.base import CommandError
import os
from demo.models import Record


def parse_datetime(value: str) -> datetime:
    return datetime.strptime(value, "%Y%m%d%H%M%S")


def extract_values(path: str):
    data: List[dict] = []
    with open(path, "r") as file:
        file.readline()
        for index, line in enumerate(file.readlines()):
            parts = line.split(",")
            try:
                data.append({
                    "nmi": parts[1],                    
                    "meter_serial_number": parts[6],                    
                    "read": parts[13],                    
                    "date": parts[14],
                    "file_name": os.path.basename(path)   
                })
            except IndexError:
                raise CommandError("There is error while extracting data from CSV (line {})".format(index+1))
    return data


def create_record_from_values(data) -> Record:
    data["date"] = parse_datetime(data["date"])
    record = Record(**data)
    record.save()
    return record