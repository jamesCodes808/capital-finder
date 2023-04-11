from urllib import parse
import requests

url_components = parse.urlsplit("https://capital-finder-mike.vercel.app/api/capital-finder?capital=Chile")
# Result is:
# SplitResult(scheme='https', netloc='capital-finder-mike.vercel.app', path='/api/capital-finder', query='capital=Chile', fragment='')

query_string_list = parse.parse_qsl(url_components.query)
# Result is:
# [('capital', 'Chile')]

dic = dict(query_string_list)
# Result is:
# {'capital': 'Chile'}

url = "https://restcountries.com/v3.1/name/" + dic["capital"]
# Result is:
# https://restcountries.com/v3.1/name/Chile

data = requests.get(url)
# Result is a http response

data = data.json()
# Result is:
'''
[{'name': {'common': 'Chile', 'official': 'Republic of Chile', 'nativeName': {'spa': {'official': 'República de Chile', 'common': 'Chile'}}}, 'tld': ['.cl'], 'cca2': 'CL', 'ccn3': '152', 'cca3': 'CHL', 'cioc': 'CHI', 'independent': True, 'status': 'officially-assigned', 'unMember': True, 'currencies': {'CLP': {'name': 'Chilean peso', 'symbol': '$'}}, 'idd': {'root': '+5', 'suffixes': ['6']}, 'capital': ['Santiago'], 'altSpellings': ['CL', 'Republic of Chile', 'República de Chile'], 'region': 'Americas', 'subregion': 'South America', 'languages': {'spa': 'Spanish'}, 'translations': {'ara': {'official': 'جمهورية تشيلي', 'common': 'تشيلي'}, 'bre': {'official': 'Republik Chile', 'common': 'Chile'}, 'ces': {'official': 'Chilská republika', 'common': 'Chile'}, 'cym': {'official': 'Gweriniaeth Chile', 'common': 'Chile'}, 'deu': {'official': 'Republik Chile', 'common': 'Chile'}, 'est': {'official': 'Tšiili Vabariik', 'common': 'Tšiili'}, 'fin': {'official': 'Chilen tasavalta', 'common': 'Chile'}, 'fra': {'official': 'République du Chili', 'common': 'Chili'}, 'hrv': {'official': 'Republika Čile', 'common': 'Čile'}, 'hun': {'official': 'Chilei Köztársaság', 'common': 'Chile'}, 'ita': {'official': 'Repubblica del Cile', 'common': 'Cile'}, 'jpn': {'official': 'チリ共和国',mon': 'チリ'}, 'kor': {'official': '칠레 공화국', 'common': '칠레'}, 'nld': {'official': 'Republiek Chili', 'common': 'Chili'}, 'per': {'official': 'جمهوری شیلی', 'common': 'شیلی'}, 'fficial': 'Republika Chile', 'common': 'Chile'}, 'por': {'official': 'República do Chile', 'common': 'Chile'}, 'rus': {'official': 'Республика Чили', 'common': 'Чили'}, 'slk': {'offic
ial': 'Čílska republika', 'common': 'Čile'}, 'spa': {'official': 'República de Chile', 'common': 'Chile'}, 'srp': {'official': 'Република Чиле', 'common': 'Чиле'}, 'swe'             '
: {'official': 'Republiken Chile', 'common': 'Chile'}, 'tur': {'official': 'Şili Cumhuriyeti', 'common': 'Şili'}, 'urd': {'official': 'جمہوریہ چلی', 'common': 'چلی'}, 'zho': {'officia
l': '智利共和国', 'common': '智利'}}, 'latlng': [-30.0, -71.0], 'landlocked': False, 'borders': ['ARG', 'BOL', 'PER'], 'area': 756102.0, 'demonyms': {'eng': {'f': 'Chilean', 'm': 'Chi
lean'}, 'fra': {'f': 'Chilienne', 'm': 'Chilien'}}, 'flag': '🇨🇱', 'maps': {'googleMaps': 'https://goo.gl/maps/XboxyNHh2fAjCPNn9', 'openStreetMaps': 'https://www.openstreetmap.org/re
lation/167454'}, 'population': 19116209, 'gini': {'2017': 44.4}, 'fifa': 'CHI', 'car': {'signs': ['RCH'], 'side': 'right'}, 'timezones': ['UTC-06:00', 'UTC-04:00'], 'continents': ['So
uth America'], 'flags': {'png': 'https://flagcdn.com/w320/cl.png', 'svg': 'https://flagcdn.com/cl.svg', 'alt': 'The flag of Chile is composed of two equal horizontal bands of white an
d red, with a blue square of the same height as the white band superimposed in the canton. A white five-pointed star is centered in the blue square.'}, 'coatOfArms': {'png': 'https://
mainfacts.com/media/images/coats_of_arms/cl.png', 'svg': 'https://mainfacts.com/media/images/coats_of_arms/cl.svg'}, 'startOfWeek': 'monday', 'capitalInfo': {'latlng': [-33.45, -70.67]}, 'postalCode': {'format': '#######', 'regex': '^(\\d{7})$'}}]

country = data[0]['name']['common']
# result is 
# Chile