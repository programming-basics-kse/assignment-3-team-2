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

def file_line_to_medal(header, line): #modifies result_medals and total_medals
    line = line.split('\t')
    params = {header[i]: line[i] for i in range(len(header))}
    return Medal(params)

