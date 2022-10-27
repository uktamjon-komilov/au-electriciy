import pytest
from demo.utils import parse_datetime
from django.utils import timezone


def test_parse_datetime_works():
    assert parse_datetime("20040107100333") == timezone.datetime(2004, 1, 7, 10, 3, 33)
    assert parse_datetime("20040103094843") == timezone.datetime(2004, 1, 3, 9, 48, 43)
    assert parse_datetime("20040104141941") == timezone.datetime(2004, 1, 4, 14, 19, 41)