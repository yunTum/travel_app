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

class PlaceName(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place

class Card(models.Model):
    place = models.ForeignKey(PlaceName, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    CHARA_SET = (
        ("characteristic", "特徴"),
        ("landscape", "風景"),
        ("history", "歴史"),
        ("theme park", "遊園地"),
        ("leisure facilities", "レジャー施設"),
        ("sports", "スポーツ"),
        ("food", "食事処"),
        ("spring", "温泉"),
        ("amusement", "娯楽"),
        ("nature", "自然"),
        ("art", "芸術"),
        ("world heritage", "世界遺産"),
        ("souvenir", "お土産"),
    )
    chara = models.CharField(choices=CHARA_SET, default="characteristic", max_length=18)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    duration = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    explain = models.TextField(max_length=500)

    def __str__(self):
        return  self.place

class CardToCard(models.Model):
    choice_place = models.ForeignKey(PlaceName, on_delete=models.CASCADE)
    duration = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.choice_place + " -> " + self.choice_place