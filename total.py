from medal import Medal

class CountryStats:
    def __init__(self, country: str):
        self.country = country
        self.medals = {
            'gold': 0,
            'silver': 0,
            'bronze': 0
        }

    def add_medal(self, medal: Medal):#takes a medal, updates stats
        if medal.get_medal_type() == 'NA':
            return
        self.medals[medal.get_medal_type()] += 1

def process(options) -> str :
    pass
