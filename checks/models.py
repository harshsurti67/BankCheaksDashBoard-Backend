# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

# class Check(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     check_number = models.CharField(max_length=50)
#     payer_name = models.CharField(max_length=100)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date_received = models.DateField()
#     memo = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return f"Check #{self.check_number} from {self.payer_name}"a
from django.db import models
from django.contrib.auth.models import User

class Check(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_number = models.CharField(max_length=50)
    payer_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField()
    memo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Check #{self.check_number} from {self.payer_name}"