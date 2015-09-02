from .models import MarketingSource, GuestCard
from .forms import GuestCardForm
from .exceptions import DataLoadError

def load_data_from_json(data):
    '''Accepts data in json format and injests data into relational database
    '''
    try:
        # fetch once and use for membership check
        existing_cards = set(GuestCard.objects.values_list('gc_id', flat=True))
        for card in data:
            if int(card.get('id')) in existing_cards:
                continue 
            card['gc_id'] = card.pop('id')
            # lets keep marketing source out for now and create an instance of
            # GuestCard using remaining data. 
            if card.get('marketing_source'):
                # if there is a marketing source, find the associated instance in the database.
                ms_instance, new = MarketingSource.objects.get_or_create(name=card.pop('marketing_source'))
                card['marketing_source'] = ms_instance.id
            guest_card_form = GuestCardForm(card)
            if guest_card_form.is_valid():
                guest_card_form.save()
    except Exception as e:
        raise DataLoadError(str(e))
        
        
  
