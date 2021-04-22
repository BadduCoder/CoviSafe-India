from django.db import models

class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Address(Common):

    address_line_1 = models.CharField(max_length=264)
    address_line_2 = models.CharField(max_length=264, null=True, blank=True)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=64)
    pincode = models.IntegerField(max_length=6)

    def __str__(self):
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}"