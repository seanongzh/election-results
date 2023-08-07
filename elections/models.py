from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.template.defaultfilters import slugify
from positions.models import Position
import datetime

class Election(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()
    is_special = models.BooleanField("special election", default=False)
    slug = models.SlugField(default="", unique=True)

    def __str__(self):
        match self.is_special:
            case True:
                special = " (Special)"
            case _:
                special = ""
        return str(self.year) + " " + str(self.position) + special
    
    def get_absolute_url(self):
        return reverse("election-detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self)) # autoset slug; excluded from admin form
        return super().save(*args, **kwargs)
    
    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(year__lte=datetime.date.today().year), name="year_lte_now"),
            models.UniqueConstraint("position", "year", "is_special", name="unique_election")
        ]
        ordering = ["-year", "position", "is_special"]