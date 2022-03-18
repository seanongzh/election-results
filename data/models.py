from django.db import models
from django.contrib.postgres.fields import ArrayField

class Candidate(models.Model):
    first = models.CharField(max_length=255, blank=True, null=True)
    last = models.CharField(max_length=255)
    middle = models.CharField(max_length=2, blank=True, null=True)
    suffix = models.CharField(max_length=5, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    aka = ArrayField(models.CharField(max_length=255), blank=True, null=True)

    class Meta:
        db_table = 'candidates'

    def __str__(self):
        return self.full_name


class ElectedPosition(models.Model):
    class PositionLevel(models.TextChoices):
        MUNICIPAL = 'municipal'
        COUNTY = 'county'
        STATE = 'state'
        NATIONAL = 'national'

    name = models.CharField(max_length=255)
    level = models.CharField(max_length=9, choices=PositionLevel.choices, default=PositionLevel.MUNICIPAL)
    eliminated_in = models.IntegerField(blank=True, null=True)
    replaced_with = models.OneToOneField('self', models.CASCADE, db_column='replaced_with', blank=True, null=True)
    primary = models.BooleanField(default=False)

    class Meta:
        db_table = 'elected_positions'

    def __str__(self):
        return self.name


class Election(models.Model):
    year = models.IntegerField()
    position = models.ForeignKey(ElectedPosition, models.PROTECT)
    unexpired_term_length = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'elections'
    
    def __str__(self):
        return "%s %s%s" \
            %(str(self.position), \
              str(self.year), \
              "" if self.unexpired_term_length is None else " (Unexpired: %s)" %(str(self.unexpired_term_length)))


class Party(models.Model):
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'parties'
        verbose_name_plural = 'Parties'
    
    def __str__(self):
        return self.name


class Result(models.Model):
    election = models.ForeignKey(Election, models.PROTECT)
    candidate = models.ForeignKey(Candidate, models.PROTECT)
    party = models.ForeignKey(Party, models.PROTECT, blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)
    municipal_winner = models.BooleanField(blank=True, null=True)
    overall_winner = models.BooleanField(blank=True, null=True)
    incumbent = models.BooleanField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'results'
        constraints = [models.UniqueConstraint(fields=['election','candidate'], name='unique_result')]
    
    def __str__(self):
        return "%s for %s" %(str(self.candidate), str(self.election))
