class Medal:
    def __init__(self, params):
        self.params = params

    def display(self) -> str:
        return f'{self.get_name()} - {self.get_event()} - {self.get_medal_type()}\n'

    def get_country(self) -> str:
        return self.params['team']
    
    def get_noc(self) -> str:
        return self.params['noc']

    def get_medal_type(self) -> str:
        return self.params['medal']

    def get_name(self) -> str:
        return self.params['name']

    def get_event(self) -> str:
        return self.params['event']

    def get_year(self) -> str:
        return self.params['year']
