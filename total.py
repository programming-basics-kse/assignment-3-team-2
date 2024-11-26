from medal import file_line_to_medal
from medal import Medal

class CountryStats:
    def __init__(self, country: str):
        self.country = country
        self.medals = {
            'gold': 0,
            'silver': 0,
            'bronze': 0
        }

    def add_medal(self, medal: Medal):
        if medal.get_medal_type() == 'NA':
            return
        self.medals[medal.get_medal_type()] += 1

def format_output(countries) -> str:
    pass

def process(options) -> str :
    countries = {}

    with open(options.file, 'r') as file:
        line = file.readline().replace('\n', '').split('\t')
        header = [i.lower() for i in line]
        
        line = file.readline().replace('\n', '')
        while line:
            medal = file_line_to_medal(line)
            if medal.get_year() == options.year:  
                country = medal.get_country()
                if not country in countries:
                    countries[country] = CountryStats(country)
                countries[country].add_medal(medal)
            
            line = file.readline().replace('\n', '')
