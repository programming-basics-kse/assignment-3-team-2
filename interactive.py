from actions import overall
from medal import file_line_to_medal
from medal import Medal

class CountryStats:
    def __init__(self, country):
        self.country = country
        self.most_medals = {'year': None, 'total_medals': 0}
        self.least_medals = {'year': None, 'total_medals': 0}
        self.data = {
            'year': {
                'place': None,
                'total_medals': 0,
                'medals': {'gold': 0, 'silver': 0, 'bronze': 0}
            }
        }

    def add_medal(self, medal):
        if medal.get_medal_type() == 'NA' or self.country != options.countries:
            return
        year = medal.get_year()
        total_medals = self.data[year]['total_medals']

        self.data[year]['medals'][medal.get_medal_type] += 1
        total_medals += 1

        if total_medals > self.most_medals['total_medals']:
            self.most_medals['total_medals'] = total_medals
            self.most_medals['year'] = year
        if total_medals < self.least_medals['total_medals']:
            self.least_medals['total_medals'] = total_medals
            self.least_medals['year'] = year

    def get_best_games(self) -> str:
        return f"Best games: {self.most_medals['year']} - {self.most_medals['total_medals']} medals\n"

    def get_worst_games(self) -> str:
        return f"Worst games: {self.least_medals['year']} - {self.least_medals['total_medals']} medals\n

    def get_average_medals(self) -> str:
        overall_years = len(self.data)
        overall_medals = sum(self.data[year]['total_medals'] for year in self.data)
        average_medals = round(overall_medals / overall_years, 2)
        return f'Average medals: {average_medals}\n'


    def get_first_participation(self) -> str:
        first_year = min(self.data.keys())
        return f"First participation: {first_year} {self.data['year']['place']}\n"

def format_output(stats):
    output = f'The first olympics participation: {stats.get_first_participation()\n}'
    output += f'The best performance: {stats.get_best_games()}\n'
    output += f'The worst performance: {stats.get_worst_games()}\n'
    output += stats.get_average_medals()
    
    return output

def process_country(country, options):
    stats = CountryStats(country)

    with open(options.file, 'r') as file:
        line = file.readline().replace('\n', '').split('\t')
        header = [i.lower() for i in line]

        line = file.readline().replace('\n', '')
        while line:
            medal = file_line_to_medal(header, line)
            stats.add_medal()
            line = file.readline().replace('\n', '')

    return format_output(stats)

def process(options):
    output = ''
    print('Type q to exit')
    inp = input('(Country) ')
    while inp != q:
        result = process_country(inp, options)
        print(result, end='')
        output += result
