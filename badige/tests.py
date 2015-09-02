import os
import json
from django.test import TestCase
from badige.load_data import load_data_from_json
from badige import marketing_insights
from badige.models import GuestCard, MarketingSource

class LoadDataTest(TestCase):

    def test_load_data(self):
        data = json.load(open('%s/fixtures/guest_cards.json' % os.path.dirname(os.path.realpath(__file__))))
        load_data_from_json(data)
        self.assertEquals(GuestCard.objects.count(), 523)
        self.assertEquals(MarketingSource.objects.get(name='Apartment Guide'
                                 ).guestcard_set.count(), 133)
         

    def test_roi_calculation(self):
        grouping_data = {'leases': 2, 'first_seen_quarter': 'Q3 2013', 'leads': 2}
        self.assertEquals(marketing_insights.apartment_guide(grouping_data)['investment'], 1485.0)
        self.assertEquals(marketing_insights.apartment_guide(grouping_data)['cost_per_lead'], 742.5)
       
        self.assertEquals(marketing_insights.apartments_dot_com(grouping_data)['investment'], 590.0)
        self.assertEquals(marketing_insights.apartments_dot_com(grouping_data)['cost_per_lead'], 295.0)

        self.assertEquals(marketing_insights.rent_dot_com(grouping_data)['investment'], 1190.0)
        self.assertEquals(marketing_insights.rent_dot_com(grouping_data)['cost_per_lead'], 595.0)

        self.assertEquals(marketing_insights.for_rent(grouping_data)['investment'], 635.0)
        self.assertEquals(marketing_insights.for_rent(grouping_data)['cost_per_lead'], 610.0)

        self.assertEquals(marketing_insights.resident_referral(grouping_data)['investment'], 1000.0)
        self.assertEquals(marketing_insights.resident_referral(grouping_data)['cost_per_lead'], 500.0)








