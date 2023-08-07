from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Party(models.Model):
    party_name = models.CharField(max_length=255, unique=True)
    party_demonym = models.CharField(max_length=255)
    slug = models.SlugField(default="", unique=True)

    def __str__(self):
        return self.party_name
    
    def get_absolute_url(self):
        return reverse("party-detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.party_name.replace("Party", "")) # autoset slug; excluded from admin form
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "parties"
        ordering = ["party_name"]