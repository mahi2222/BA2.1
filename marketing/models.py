from django.db import models

class BusinessAssociate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    fee_ready_to_pay = models.IntegerField(help_text="Amount in INR (1000 - 10000)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
