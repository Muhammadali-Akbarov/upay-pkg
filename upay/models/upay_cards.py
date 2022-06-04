from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UpayCardsModel(models.Model):
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, null=False, blank=False)
    card_exp_date = models.CharField(max_length=5, null=False, blank=False)
    card_cvv = models.CharField(max_length=3, null=False, blank=False)
    card_holder_name = models.CharField(max_length=100, null=False, blank=False)
    holder_phone_number = models.CharField(max_length=15, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.client_id
