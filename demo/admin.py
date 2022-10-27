from django.contrib import admin

from demo.models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ["nmi", "meter_serial_number", "read", "date", "file_name"]
    list_display_links = ["nmi", "meter_serial_number"]
    search_fields = ["nmi", "meter_serial_number"]


admin.site.register(Record, RecordAdmin)
