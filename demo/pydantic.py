from pydantic import BaseModel, ValidationError, validator


class Nem13Model(BaseModel):
    record_indicator: int
    nmi: str
    nmi_configuration: str
    register_id: str
    nmi_suffix: str
    MDMDataStreamIdentifier: str
    MeterSerialNumber: str
    DirectionIndicator: str
    PreviousRegisterRead: str
    PreviousRegisterReadDateTime: str
    PreviousQualityMethod: str
    PreviousReasonCode: str
    PreviousReasonDescription: str
    CurrentRegisterRead: str
    CurrentRegisterReadDateTime: str
    CurrentQualityMethod: str
    CurrentReasonCode: str
    CurrentReasonDescription: str
    Quantity: str
    UOM: str
    NextScheduledReadDate: str
    UpdateDateTime: str
    MSATSLoadDateTim: str

    @validator("record_indicator")
    def record_indicator_max_length(cls, value):
        if len(str(value)) != 3:
            raise ValidationError("'record_indicator' must be 3 digits long")
        return value

    @validator("nmi")
    def nmi_max_length(cls, value):
        if len(value) != 3:
            raise ValidationError("'nmi' must be 10 chars long")
        return value