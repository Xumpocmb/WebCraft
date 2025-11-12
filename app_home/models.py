from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_svg = models.TextField(help_text="SVG code for the service icon")
    tagline = models.CharField(max_length=200, blank=True, null=True, help_text="Short tagline for the service (e.g., 'Идеально для стартапов')")

    def __str__(self):
        return self.title
        return self.title
