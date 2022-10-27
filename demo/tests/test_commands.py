from django.core.management import call_command
from django.test import TestCase
import os
from django.conf import settings
from demo.models import Record


class LoadNEM13FilesCommandsTestCase(TestCase):
    def test_mycommand(self):
        "Test `load_nem13` command"

        args = [os.path.join(settings.BASE_DIR, "demo", "tests", "fixtures", "data.csv")]
        opts = {}

        call_command("load_nem13", *args, **opts)

        last_records = Record.objects.all().order_by("-id")[:3]

        assert last_records[0].nmi == "6622677625"
        assert last_records[1].nmi == "7142747824"
        assert last_records[2].nmi == "2291137510"