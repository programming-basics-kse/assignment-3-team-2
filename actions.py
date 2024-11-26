from medals import Medal


RESULT_MEDALS_CAP = 10

def process_line(header, line, options, result_medals, total_medals): #modifies result_medals and total_medals
    line = line.split('\t')
    params = {header[i]: line[i] for i in range(len(header))}
    medal = Medal(params)
    
    if options.country in [medal.get_noc(), medal.get_country()]:
        medal_type = medal.get_medal_type()
        if medal_type != 'NA':
            total_medals[medal_type.lower()] += 1
            if len(result_medals) < RESULT_MEDALS_CAP:
                result_medals.append(medal)

def format_output(result_medals, total_medals):
    output = ''
    for medal in result_medals:
        output += medal.display()
    return f'{output}\nTotal gold: {total_medals['gold']}\nTotal silver: {total_medals['silver']}\nTotal bronze: {total_medals['bronze']}'

def medals(options):
    result_medals = []
    total_medals = {
        'gold': 0,
        'silver': 0,
        'bronze': 0,
    }

    with open(options.file, 'r') as file:
        line = file.readline()
        header = [i.lower() for i in line.replace('\n', '').split('\t')]

        line = file.readline()
        line.replace('\n', '')
        while line:
            process_line(header, line, options, result_medals, total_medals)
            line = file.readline().replace('\n', '')
    print(result_medals)
    print(total_medals)            
    return format_output(result_medals, total_medals)
