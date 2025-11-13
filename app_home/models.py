from decimal import Decimal
from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_svg = models.TextField(help_text="SVG code for the service icon")
    tagline = models.CharField(max_length=200, blank=True, null=True, help_text="Short tagline for the service (e.g., 'Идеально для стартапов')")

    def __str__(self):
        return str(self.title)

class Price(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # This will now be the original price
    recommended = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    icon_svg = models.TextField(help_text="SVG code for the price icon", blank=True, null=True)

    @property
    def discounted_price(self):
        if self.price is not None and self.discount_percentage is not None:
            return self.price * (Decimal('1') - self.discount_percentage / Decimal('100'))
        return None

    @property
    def display_price(self):
        if self.discounted_price is not None:
            return f"{self.discounted_price:.0f}"
        elif self.price is not None:
            return f"{self.price:.0f}"
        return "Цена не указана"

    def __str__(self):
        return str(self.title)

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, help_text="Phone number or Email address")
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('processed', 'Обработана'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"

    def __str__(self):
        return f"Contact from {self.name} at {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"

class ContactInfo(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)
    telegram_link = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return "Contact Information"
