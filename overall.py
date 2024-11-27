from medal import file_line_to_medal
from medal import Medal

def format_output(result) -> str:
    return '\n'.join([f'{i}: Best year: {result[i][0]}, Won medals: {result[i][1]}' if result[i][0] != None else f'The country {i} was not found in the dataset' for i in result])

def process(options):#options.countries = ['Ukraine', 'Romania']
    result = {} #country: [best_year, n_medals]
    countries = {i: {} for i in options.countries}

    with open(options.file, 'r') as file:
        line = file.readline().replace('\n', '').split('\t')
        header = [i.lower() for i in line]

        line = file.readline().replace('\n', '')
        while line:
            medal = file_line_to_medal(header, line)
            if medal.get_country() in options.countries and medal.get_medal_type() != 'NA':
                year = medal.get_year()
                country = medal.get_country()
                if year not in countries[country]:
                    countries[country][year] = 0
                countries[country][year] += 1

            line = file.readline().replace('\n', '')

    for country, years in countries.items():
        best_year = None
        max_medals = 0
        for year, medals in years.items():
            if medals > max_medals:
                max_medals = medals
                best_year = year
        result[country] = [best_year, max_medals]

    return format_output(result)
