class CountryStats:
    def __init__(self, country):
        self.country = country
        # data = {
        #    year: {
        #       place: value,
        #       medals: {gold: n, silver: n, bronze: n}
        #   }
        #}

    def add_medal(self):
        pass

    def get_best_games(self) -> str:
        pass

    def get_worst_games(self) -> str:
        pass

    def get_average_medals(self) -> str:
        pass

    def get_first_participation(self) -> str:
        pass

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
    
