def fetch_lines_from_file(file):
    pass

def filter_lines(lines, country, year):
    pass

def format_output():
    pass

def medals(options):
    lines = fetch_lines_from_file(options.file)
    filtered = filter_lines(lines, options.country, options.year)
    
    return format_output(filtered)
