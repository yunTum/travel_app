from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    STATUS_TAKEAWALK = "take a walk"
    STATUS_DATEPLAN = "date plan"
    STATUS_FAMILYTRIP = "family trip"
    STATUS_SET = (
            (STATUS_TAKEAWALK, "散歩"),
            (STATUS_DATEPLAN, "デート"),
            (STATUS_FAMILYTRIP, "家族旅行"),
    )
    status = models.CharField(choices=STATUS_SET, default=STATUS_TAKEAWALK, max_length=12)
    def __str__(self):
        return self.name
