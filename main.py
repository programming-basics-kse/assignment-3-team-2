from argparse import ArgumentParser, Namespace
from pathlib import Path
import actions

def setup_arg_parser():
    parser = ArgumentParser(
        prog='main.py',
        description='This program fetches data from you dataset!'
    )

    parser.add_argument('--output', type=Path, default=None, help='File to write output to')

    parser.add_argument('input_file', type=Path, help='Input file to process')
    
    subparsers = parser.add_subparsers(dest='action', help='Action to perform')

    medals_parser = subparsers.add_parser('medals', help='Get first 10 medals and total stats')
    medals_parser.add_argument('country', type=str, help='Country name or NOC')
    medals_parser.add_argument('year', type=int, help='Year of the games')

    total_parser = subparsers.add_parser('total', help='Get stats of every country that won at least one medal')
    total_parser.add_argument('year', type=int, help='Year of the games')

    overall_parser = subparsers.add_parser('overall', help='Print the years input countries had the most medals')
    overall_parser.add_argument('countries', type=str, nargs='+', help='Countries to be analized')
    
    interactive_parser = subparsers.add_parser('interactive', help='Get country stats in interactive mode')

    return parser

def action_and_options_from_args(args):
    options = Namespace()
    options.file = args.input_file
    if args.action == 'medals':
        options.country = args.country
        options.year = args.year
    elif args.action == 'total':
        options.year = args.year
    elif args.action == 'overall':
        options.countries = args.countries
    
    return args.action, options

def main():
    arg_parser = setup_arg_parser()
    args = arg_parser.parse_args()

    action, options = action_and_options_from_args(args)
    action = getattr(actions, action)

    output = action(options)
    if args.action != 'interactive': 
        print(output)

    if args.output != None:
        with open(args.output, 'w') as file:
            file.write(output)    


if __name__ == '__main__':
    main()
