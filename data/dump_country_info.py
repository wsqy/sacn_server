import os
import sys
import json
from scanBase.models import CountryInfo
with open(os.path.join('data','iso-3166-1.json')) as f:
    data_list = json.loads(f.read())


for data in data_list:
    country = CountryInfo()
    country.country_cn = data.get('country-cn','')[:28]
    country.country_en = data.get('country-en','')[:28]
    country.letter2 = data.get('letter-2','')
    country.letter3 = data.get('letter-3','')
    country.digital_code = data.get('digital-code','')
    country.ISO_3166_2_code = data.get('ISO 3166-2-code','')[:28]
    country.save()
