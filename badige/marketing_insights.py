""" This module has methods that take grouping data from the database that looks like this
{'leases': 13, 'first_seen_quarter': 'Q3 2013', 'leads': 47, 'marketing_source': 27}
and return total cost of marketing and ROI on money spent (per lead)"""

def apartment_guide(result):
    return {'investment': 495.0 * 3, 
            'cost_per_lead': (495.0 * 3)/result['leads']
           }

def apartments_dot_com(result):
    return {'investment': 295.0 * result['leases'],
            'cost_per_lead': (295.0 * result['leases'])/result['leads']
           }

def rent_dot_com(result):
    # TODO:  cost per lease is $595 or 50%, whichever is higher
    # Find a way to compute 50% of rent per lease
    return {'investment': 595.0 * result['leases'],
            'cost_per_lead': (595.0 * result['leases'])/result['leads']
           }

def for_rent(result):
    return {'investment': (195.0 * 3) + (25.0 * result['leads']),
            'cost_per_lead': (195.0 * 3) + (25.0 * result['leads'])/result['leads']
           }

def resident_referral(result):
    return {'investment': 500.0 * result['leases'],
            'cost_per_lead': (500.0 * result['leases'])/result['leads']
           }
