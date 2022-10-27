from django.db import models


class Record(models.Model):
    # NMI for the connection point. Does not include check-digit or NMI suffix
    nmi = models.CharField(max_length=10)

    # Meter Serial ID as per Standing Data for MSATS.
    meter_serial_number = models.CharField(max_length=12)

    # Register read.
    # Example of values: 1234567.123 or 0012456.123.
    read = models.CharField(max_length=15)

    # Actual date/time of the Meter Reading.
    date = models.DateTimeField()

    # The filename of the flow file
    file_name = models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.meter_serial_number, self.date)