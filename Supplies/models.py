from django.db import models
from Common.models import BaseModel


class Supply(BaseModel):

    PLASMA = "PLM"
    BLOOD = "BLD"
    OXYGEN = "OXY"
    HOME_FOOD = "HFD"
    HOSPITAL_BED = "HBD"
    ICU_BED = "ICU"

    SUPPLY_TYPES = (
        (PLASMA, "Plasma"),
        (BLOOD, "Blood"),
        (OXYGEN, "OXYGEN"),
        (HOME_FOOD, "Home Food"),
        (HOSPITAL_BED, "Hospital Bed"),
        (ICU_BED, "ICU Bed")
    )

    CONCENTRATOR = "CON"
    REFILL = "REF"
    EMPTY_CYL = "EMP"
    FILLED_CYL = "FIL"

    OXYGEN_SUPPLY_TYPES = (
        (CONCENTRATOR, "Concentrator"),
        (REFILL, "Refill"),
        (EMPTY_CYL, "Empty Cylinder"),
        (FILLED_CYL, "Filled Cylinder")
    )

    MY_CONTACT = "MY_CONTACT"
    WRONG_CONTACT = "WRONG_CONTACT"
    VERIFIED_WRONG = "VERIFIED_WRONG"
    OTHER = "OTHER"
    SPAM_REASON_OPTIONS = (
        (MY_CONTACT, "My Contact"),
        (WRONG_CONTACT, "Wrong Contact"),
        (VERIFIED_WRONG, "Verified wrong information"),
        (OTHER, "Some other reason")
    )

    supply_type = models.CharField(max_length=3, choices=SUPPLY_TYPES)
    supply_desc = models.CharField(max_length=264)
    primary_contact = models.CharField(max_length=10)
    secondary_contact = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    supplier_name = models.CharField(max_length=128)
    address = models.ForeignKey(to='Common.Address', on_delete=models.CASCADE)

    # Requirement specific fields
    blood_group = models.CharField(max_length=4, null=True, blank=True)
    oxygen_supply_type = models.CharField(max_length=3, choices=OXYGEN_SUPPLY_TYPES, null=True, blank=True)
    icu_bed_count = models.IntegerField(default=-1)
    normal_bed_count = models.IntegerField(default=-1)

    # Report Genuine attributes
    spam_report_count = models.IntegerField(default=0)
    spam_reason = models.CharField(max_length=14, choices=SPAM_REASON_OPTIONS, null=True, blank=True)
    other_spam_reason = models.CharField(max_length=1024, null=True, blank=True)
    unavailable_report_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.supplier_name} - {self.supply_type}"