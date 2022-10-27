import pytest
from demo.utils import parse_datetime, extract_values, create_record_from_values
from django.utils import timezone
import os
from django.conf import settings


def test_parse_datetime_works():
    assert parse_datetime("20040107100333") == timezone.datetime(2004, 1, 7, 10, 3, 33)
    assert parse_datetime("20040103094843") == timezone.datetime(2004, 1, 3, 9, 48, 43)
    assert parse_datetime("20040104141941") == timezone.datetime(2004, 1, 4, 14, 19, 41)


def test_extract_values_works():
    path: str = os.path.join(settings.BASE_DIR, "demo", "tests", "fixtures", "test.csv")
    data: List[dict] = extract_values(path)

    row = data[0]

    assert row["nmi"] == "7142747824"
    assert row["meter_serial_number"] == "DYRGBH6BWPT5"
    assert row["read"] == "99772.0"
    assert row["date"] == parse_datetime("20040103094843")


@pytest.mark.django_db
def test_create_record_from_values():
    path: str = os.path.join(settings.BASE_DIR, "demo", "tests", "fixtures", "test.csv")
    data: List[dict] = extract_values(path)
    record = create_record_from_values(data[0])

    assert record.id < 999
    assert record.nmi == "7142747824"
    assert record.meter_serial_number == "DYRGBH6BWPT5"
    assert record.read == "99772.0"
    assert record.date == parse_datetime("20040103094843")
    assert record.file_name == "test.csv"
