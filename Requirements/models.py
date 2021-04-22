from django.db import models
from Common.models import Common


class Requirement(Common):

    PLASMA = "PLM"
    BLOOD = "BLD"
    OXYGEN = "OXY"


    REQUIREMENT_TYPES = (
        (PLASMA, "Plasma"),
        (BLOOD, "Blood"),
        (OXYGEN, "OXYGEN")
    )

    requirement_type = models.CharField(max_length=3,choices=REQUIREMENT_TYPES)
    requirement_desc = models.CharField(max_length=64)
    primary_contact = models.IntegerField(max_length=10)
    secondary_contact = models.IntegerField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    patient_name = models.CharField(max_length=128)
    fulfilled = models.BooleanField(default=False)
    quantity = models.CharField(max_length=10)
    address = models.ForeignKey(to='Common.Address', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.requirement_type} for {self.patient_name}"