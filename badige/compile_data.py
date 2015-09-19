import sys
from django.db.models import Count
from .models import GuestCard, MarketingSource
from .marketing_source_registry import MARKETING_SOURCE_REGISTRY

MARKETING_SOURCE_NAMES = {m.id: m.name for m in MarketingSource.objects.all()}


def compile_best_marketing_roi(quarter, year, print_data=False):
    # we are not JOINing on the DB, instead we are matching marketing_source_id to its name in memory
    first_seen_by_quarter = GuestCard.objects.filter(first_seen_quarter='Q%s %s' % (quarter, year)
                              ).values('marketing_source',
                              'first_seen_quarter').annotate(leads=Count('first_seen'),
                                                             leases=Count('lease_signed'))

    result = []
    for grouping in first_seen_by_quarter:
        # find marketing source name for given marketing source id (JOIN in memory, if you will)
        marketing_source_name = MARKETING_SOURCE_NAMES.get(grouping.get('marketing_source'))
        # if we know how to compute ROI on this marketing source, lets do it
        if marketing_source_name in MARKETING_SOURCE_REGISTRY:
            roi_function = MARKETING_SOURCE_REGISTRY.get(marketing_source_name)
            roi = roi_function(grouping)
            result.append((grouping, roi, marketing_source_name))
            if print_data is True:
                print_roi(grouping, roi)
        else: continue
    if not print_data:
        return result
      

def print_roi(grouping, roi):
    sys.stdout.write('\n%s:'% grouping['first_seen_quarter'])
    sys.stdout.write('\n- %s total leads: %s, signed leases: %s, total cost: $%s, avg cost per lead: $%s\n\n' % 
                     (MARKETING_SOURCE_NAMES[grouping['marketing_source']], grouping['leads'], grouping['leases'], 
                      "%.2f" % roi['investment'], "%.2f" % roi['cost_per_lead']))
