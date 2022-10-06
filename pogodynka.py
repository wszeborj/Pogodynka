import sys
from requests import get
from json import loads
from terminaltables import AsciiTable

url = 'https://danepubliczne.imgw.pl/api/data/synop'
CITIES = ['Gdańsk', 'Łódź', 'Zakopane']


class WheatherCheck():
    '''download weather and diplay it'''

    def __init__(self, url, cities):
        self.url = url
        self.cities = cities

    def get_weather_data(self):
        '''download data from website'''
        try:
            r = get(url)
        except Exception as exc:
            print(f'There was a problem: {exc}')
            sys.exit(0)

        return loads(r.content)

    def display_table(self):
        '''display adata in table'''
        weather_data = self.get_weather_data()

        title = 'POGODA'
        table_data = [['Miasto', 'Data', 'Temperatura', 'Cisnienie'], ]

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


if __name__ == "__main__":
    pogodynka = WheatherCheck(url, CITIES)
    pogodynka.display_table()
    sys.exit(0)
