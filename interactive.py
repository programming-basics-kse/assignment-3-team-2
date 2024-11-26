class CountryStats:
    def __init__(self, country):
        self.country = country
        self.most_medals = 0
        self.least_medals = 0
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
        self.data[]

    def get_best_games(self) -> str:
        return f'{self.data[]}'

    def get_worst_games(self) -> str:
        pass

    def get_average_medals(self) -> str:
        pass

    def get_first_participation(self) -> str:
        pass

def process(options):
    pass
