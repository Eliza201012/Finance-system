from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    balance = models.DecimalField(verbose_name="Balance", max_digits=12, decimal_places=2, default=0.00)
    currency = models.CharField(verbose_name="Currency", max_length=10)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user__username