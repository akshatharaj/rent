from django import forms
from .models import GuestCard

class GuestCardForm(forms.ModelForm):
    class Meta:
        model = GuestCard
        fields = ['application_submitted', 'expected_move_in', 'first_seen', 
                  'application_denied', 'resident_rent', 'application_approved', 
                  'marketing_source', 'gc_id', 'shown_unit', 'lease_signed', 
                  'agent_id', 'unit_name', 'application_cancelled',
                  'closing_quarter','first_seen_quarter'] 

    def clean_closing_quarter(self):
        if self.cleaned_data.get('lease_signed'):
            lease_signed = self.cleaned_data.get('lease_signed')
            return 'Q%s %s' % (lease_signed.month//4 + 1, lease_signed.year)
        else: return None

    def clean_first_seen_quarter(self):
        if self.cleaned_data.get('first_seen'):
            first_seen = self.cleaned_data.get('first_seen')
            return 'Q%s %s' % (first_seen.month//4 + 1, first_seen.year)
        else: return None

