from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from parties.models import Party

class Candidate(models.Model):
    candidate_name = models.CharField(max_length=255, unique=True)
    latest_party = models.ForeignKey(Party, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(default="", unique=True)

    def __str__(self):
        return self.candidate_name
    
    def get_absolute_url(self):
        return reverse("candidate-detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.candidate_name) # autoset slug; excluded from admin form
        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ["candidate_name"]