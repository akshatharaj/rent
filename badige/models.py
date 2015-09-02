from django.db import models

class GuestCard(models.Model):
    gc_id = models.IntegerField(null=True, blank=True)
    first_seen = models.DateField(null=False, blank=False)
    expected_move_in = models.DateField(null=True, blank=True)
    shown_unit = models.DateField(null=True, blank=True)
    agent_id = models.IntegerField(null=False, blank=False)
    application_submitted = models.DateField(null=True, blank=True)
    application_approved = models.DateField(null=True, blank=True)
    application_cancelled = models.DateField(null=True, blank=True)
    application_denied = models.DateField(null=True, blank=True)    
    lease_signed = models.DateField(null=True, blank=True, db_index=True)
    resident_rent= models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=7)
    unit_name = models.CharField(null=True, blank=True, max_length=100)
    marketing_source = models.ForeignKey('MarketingSource', null=True, blank=True)    
    closing_quarter = models.CharField(max_length=7, null=True, blank=True)
    first_seen_quarter = models.CharField(max_length=7, null=True, blank=True)
    
    class Meta:
        get_latest_by = 'lease_signed'


class MarketingSource(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    

