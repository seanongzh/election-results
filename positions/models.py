from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Position(models.Model):
    MUNICIPAL = "MUN"
    DISTRICT = "DIS"
    COUNTY = "CTY"
    STATE = "STE"
    NATIONAL = "NAT"
    GOVERNMENT_LEVEL_CHOICES = [
        (MUNICIPAL, "Municipal"),
        (DISTRICT, "District"),
        (COUNTY, "County"),
        (STATE, "State"),
        (NATIONAL, "National"),
    ]
    position_name = models.CharField(max_length=255, unique=True)
    government_level = models.CharField(max_length=3, choices=GOVERNMENT_LEVEL_CHOICES, default=MUNICIPAL)
    slug = models.SlugField(default="", unique=True)

    def __str__(self):
        return self.position_name
    
    def get_absolute_url(self):
        return reverse("position-detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.position_name) # autoset slug; excluded from admin form
        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ["position_name"]