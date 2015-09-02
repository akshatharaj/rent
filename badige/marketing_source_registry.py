from badige import marketing_insights

"""
This dictionary maps marketing source names to functions that are capable of computing 
ROI on available data
"""
MARKETING_SOURCE_REGISTRY = {'Apartments.com': marketing_insights.apartments_dot_com,
                             'Apartment Guide': marketing_insights.apartment_guide,
                             'Resident Referral': marketing_insights.resident_referral,
                             'For Rent': marketing_insights.for_rent,
                             'Rent.com': marketing_insights.rent_dot_com}
