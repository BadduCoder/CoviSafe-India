from django.db import models
from Common.models import BaseModel


class Supply(BaseModel):

    PLASMA = "PLM"
    BLOOD = "BLD"
    OXYGEN = "OXY"
    HOME_FOOD = "HFD"

    SUPPLY_TYPES = (
        (PLASMA, "Plasma"),
        (BLOOD, "Blood"),
        (OXYGEN, "OXYGEN"),
        (HOME_FOOD, "Home Food")
    )

    supply_type = models.CharField(max_length=3,choices=SUPPLY_TYPES)
    supply_desc = models.CharField(max_length=264)
    primary_contact = models.IntegerField()
    secondary_contact = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    supplier_name = models.CharField(max_length=128)
    quantity_remaining = models.CharField(max_length=10)
    address = models.ForeignKey(to='Common.Address', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.supplier_name} - {self.supply_type}"