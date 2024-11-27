from medal import file_line_to_medal
from medal import Medal

class CountryStats:
    def __init__(self, country):
        self.country = country
        self.most_medals = {'year': None, 'total_medals': 0}
        self.least_medals = {'year': None, 'total_medals': 0}
        self.data = {}
        self.data_template = { #each year has this
            'city': None,
            'total_medals': 0,
            'medals': {'gold': 0, 'silver': 0, 'bronze': 0}
        }

    def is_valid(self) -> bool:
        return len(self.data) > 0

    def add_medal(self, medal):
        if medal.get_medal_type() == 'NA' or self.country not in [medal.get_country(), medal.get_noc()]:
            return

        year = medal.get_year()
        if year not in self.data:
            self.data[year] = self.data_template
            self.data[year]['city'] = medal.get_city()

        self.data[year]['medals'][medal.get_medal_type().lower()] += 1
        self.data[year]['total_medals'] += 1
        total_medals = self.data[year]['total_medals']

        if total_medals > self.most_medals['total_medals']:
            self.most_medals['total_medals'] = total_medals
            self.most_medals['year'] = year
        if total_medals < self.least_medals['total_medals'] or self.least_medals['year'] == None:
            self.least_medals['total_medals'] = total_medals
            self.least_medals['year'] = year

    def get_best_games(self) -> str:
        return f"Best games: {self.most_medals['year']} - {self.most_medals['total_medals']} medals\n"

    def get_worst_games(self) -> str:
        return f"Worst games: {self.least_medals['year']} - {self.least_medals['total_medals']} medals\n"

    def get_average_medals_by_type(self, medal_type) -> str:
        overall_years = len(self.data)
        overall_medals = sum([self.data[year]['medals'][medal_type] for year in self.data])
        return int(overall_medals / overall_years)

    def get_average_medals(self) -> str:
        output = ''
        for i in ['gold', 'silver', 'bronze']:
            output += f'Average {i} medals: {self.get_average_medals_by_type(i)}\n'
        return output

    def get_first_participation(self) -> str:
        first_year = min(self.data.keys())
        return f"First participation: {first_year} {self.data[first_year]['city']}\n"

def format_output(stats):
    output = stats.get_first_participation()
    output += stats.get_best_games()
    output += stats.get_worst_games()
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
            stats.add_medal(medal)
            line = file.readline().replace('\n', '')
    
    if not stats.is_valid():
        return 'Sorry, the country you provided was not found in the dataset\n'

    return format_output(stats)

def process(options):
    output = ''
    print('Type q to exit')
    inp = input('(Country) ')
    while inp != 'q':
        result = process_country(inp, options)
        result += '-' * 10 + '\n'
        print(result, end='')
        output += inp + '\n'
        output += result
        
        inp = input('(Country) ')

    return output
