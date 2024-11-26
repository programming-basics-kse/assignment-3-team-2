class Medal:
    def __init__(self, params):
        self.params = params

    def display(self) -> str:
        pass

    def get_country(self) -> str:
        return self.params['team']
    
    def get_noc(self) -> str:
        return self.params['noc']

    def get_medal_type(self) -> str:
        return self.params['medal']
