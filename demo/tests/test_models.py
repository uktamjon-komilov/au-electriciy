import pytest
from django.utils import timezone

from demo.models import Record


@pytest.mark.django_db
def test_record_can_be_created():
    record = Record(
        nmi="2291137510",
        meter_serial_number="R4ZFLS6ZY1UV",
        read="56311.0",
        date=timezone.datetime(2004, 1, 7, 10, 3, 33),
        file_name="test.csv",
    )
    record.save()

    assert record.id < 999
    assert record.nmi == "2291137510"
    assert record.meter_serial_number == "R4ZFLS6ZY1UV"
    assert record.read == "56311.0"
    assert record.date == timezone.datetime(2004, 1, 7, 10, 3, 33)
    assert record.file_name == "test.csv"
