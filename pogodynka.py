import sys
from requests import get
from json import loads
from terminaltables import AsciiTable

url = 'https://danepubliczne.imgw.pl/api/data/synop'
CITIES = ['Gdańsk', 'Łódź', 'Zakopane']

try:
    r = get(url)
except Exception as exc:
    print(f'There was a problem: {exc}')
    sys.exit(0)

weather_data = loads(r.content)

title = 'POGODA'
table_data = [['Miasto', 'Data', 'Temperatura', 'Cisnienie'],]

for location in weather_data:
    if location['stacja'] in CITIES:
        table_data.append([
                            location['stacja'],
                            location['data_pomiaru'],
                            location['temperatura'],
                            location['cisnienie']
                            ])
table = AsciiTable(table_data, title)
print(table.table)


