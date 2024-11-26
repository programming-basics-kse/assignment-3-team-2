from medals import Medal

def process_line(line, result_medals, total_medals):
    pass

def format_output(result_medals, total_medals):
    output = ''
    for medal in result_medals:
        output += medal.display()
    return (f'{output}, '
            f'\nTotal gold: {total_medals['gold']}, '
            f'\nTotal silver: {total_medals['silver']}, '
            f'\nTotal bronze: {total_medals['bronze']}')


def medals(options):
    result_medals = []
    total_medals = {
        'gold': 0,
        'silver': 0,
        'bronze': 0,
    }

    with open(options.file, 'r') as file:
        line = file.readline()
        while line:
            process_line(line, result_medals, total_medals)            
            line = file.readline()
            
    return format_output(result_medals, total_medals)
