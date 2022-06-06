# MODEL DEFINITIONS
# For a database that stores election results 

from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

# Definition of Candidate model:
#   Stores info on all election candidates recorded in this database
#   Currently just stores names
#   TODO: Additional fields like gender, party, deceased or not?
class Candidate(models.Model):
    # Candidate must have at least a last name
    #   Useful for historical data with incomplete candidate names
    first = models.CharField("first name", max_length=255, blank=True)
    last = models.CharField("last name", max_length=255)

    # Middle initial should be stored without periods or spaces
    middle = models.CharField("middle initial", max_length=5, blank=True, \
        help_text="without periods or spaces")
    
    # Suffix should be stored with all relevant punctuation
    suffix = models.CharField("suffix", max_length=5, blank=True, \
        help_text="e.g. Jr., Sr., III")
    
    # Candidate must have a full name
    # Full name must be unique (for now)
    #   TODO: What if two unique individuals share the same full name? (unlikely)
    # TODO: Auto-generate full name based on previous fields in .save() func
    full_name = models.CharField(max_length=255, unique=True, \
        help_text="Order: First Middle Last Suffix")

    # Aliases are allowed
    #   Useful for candidates who have run under different names
    #   ArrayField is Postgres-specific
    aka = ArrayField(models.CharField(max_length=255), blank=True, \
        verbose_name="aliases", help_text="Full name format only")

    # Metadata for Candidate
    class Meta:
        # Legacy issue: because tables were created before model was defined
        #   (Applies to all models)
        db_table = "candidates"
        
        # "Latest" candidate is just most recently added
        get_latest_by = "id"
        
        # Ordered by last name, then first name etc.
        ordering = ["last", "first", "middle", "suffix"]

    # Additional model methods
    def __str__(self):
        return self.full_name
    def get_absolute_url(self):
        return reverse("data:candidate-detail", kwargs={"candidate_id" : self.id})


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
    def get_absolute_url(self):
        return reverse("data:position-detail", kwargs={"position_id" : self.id})

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
    def get_absolute_url(self):
        return reverse("data:election-detail", kwargs={"election_id" : self.id})

class Party(models.Model):
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'parties'
        verbose_name_plural = 'Parties'
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("data:party-detail", kwargs={"party_id" : self.id})


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
    def get_absolute_url(self):
        return reverse("data:election-detail", kwargs={"election_id" : self.election.id})
