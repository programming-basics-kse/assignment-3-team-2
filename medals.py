from medal import Medal
from medal import file_line_to_medal

RESULT_MEDALS_CAP = 10

def process_line(header, line, options, result_medals, total_medals): #modifies result_medals and total_medals
    medal = file_line_to_medal(header, line)   
 
    if options.country in [medal.get_noc(), medal.get_country()] and medal.get_year() == str(options.year):
        medal_type = medal.get_medal_type()
        if medal_type != 'NA':
            total_medals[medal_type.lower()] += 1
            if len(result_medals) < RESULT_MEDALS_CAP:
                result_medals.append(medal)

def format_output(result_medals, total_medals):
    if len(result_medals) == 0:
        return 'There was no records of this country and this year in the dataset'
    output = ''
    for medal in result_medals:
        output += medal.display()
    return f'{output}\nTotal gold: {total_medals["gold"]}\nTotal silver: {total_medals["silver"]}\nTotal bronze: {total_medals["bronze"]}'

def process(options):
    result_medals = []
    total_medals = {
        'gold': 0,
        'silver': 0,
        'bronze': 0,
    }

    with open(options.file, 'r') as file:
        line = file.readline().replace('\n', '').split('\t')
        header = [i.lower() for i in line]

        line = file.readline().replace('\n', '')
        while line:
            process_line(header, line, options, result_medals, total_medals)
            line = file.readline().replace('\n', '')

    return format_output(result_medals, total_medals)

