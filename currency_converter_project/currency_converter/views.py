# import requests
# from django.shortcuts import render
# from requests.structures import CaseInsensitiveDict

# def conversion_rates(request):
#     url = "https://api.freecurrencyapi.com/v1/latest"
#     base_currency = 'USD'
#     api_key = "fca_live_fYGM2jfifY16bCDf2YkFMlouP31MhBI1Tdus5piP"

#     params = {
#         "api_key": api_key,
#         "base_currency": base_currency,
#     }

#     headers = CaseInsensitiveDict()
#     headers["apikey"] = api_key

#     response = requests.get(url, params=params, headers=headers)
#     data = response.json()

#     if response.status_code == 200:
#         conversion_rates = data.get('data', {})
#         print('Great')
#     else:
#         conversion_rates = {}
#         print('Failed')

#     return render(request, 'conversion_rates.html', {'conversion_rates': conversion_rates})

# currency_converter/views.py

import requests
from django.shortcuts import render
from requests.structures import CaseInsensitiveDict
import json

def conversion_rates(request):
    url = "https://api.freecurrencyapi.com/v1/latest"
    base_currency = 'USD'
    currencies = 'GBP,HKD'
    api_key = ""

    params = {
        "base_currency": base_currency,
        'currencies': currencies,
    }

    headers = {
        "apikey": api_key,
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        conversion_rates = data.get('data', {})
    else:
        error_message = f"Error: {response.status_code} - {response.text}"
        return render(request, 'error.html', {'error_message': error_message})
        print('NOT Correct')

    return render(request, 'conversion_rates.html', {'conversion_rates': conversion_rates})
