from django.db import models

class GroceryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    is_purchased = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.quantity}) - {'✓' if self.is_purchased else '…'}"
