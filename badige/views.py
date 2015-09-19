from django.shortcuts import render
from .compile_data import compile_best_marketing_roi

def best_marketing(request, *args, **kwargs):
    year = kwargs['year']
    quarter = kwargs['quarter']
    roi_result = compile_best_marketing_roi(quarter, year)
    return render(request, 'badige/roi.html', context={'roi_result': roi_result}) 
