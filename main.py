from argparse import ArgumentParser, Namespace
from pathlib import Path
import actions

def setup_arg_parser():
    parser = ArgumentParser(
        prog='main.py',
        description='This program fetches data from you dataset!'
    )

    parser.add_argument('input_file', type=Path, help='Input file to process')
    
    subparsers = parser.add_subparsers(dest='action', help='Action to perform')

    medals_parser = subparsers.add_parser('-medals', help='Get first 10 medals and total stats')
    medals_parser.add_argument('country', type=str, help='Country name or NOC')
    medals_parser.add_argument('year', type=int, help='Year of the games')

    total_parser = subparsers.add_parser('-total', help='Get stats of every country that won at least one medal')
    total_parser.add_argument('year', type=int, help='Year of the games')
    
    return parser

def action_and_options_from_args(args):
    options = Namespace()
    options.file = args.input_file
    if args.action == 'medals':
        options.country = args.country
        options.year = args.year

        return args.action, options

def main():
    arg_parser = setup_arg_parser()
    args = arg_parser.parse_args()

    action, options = action_and_options_from_args(args)
    action = getattr(actions, action)

    output = action(options) 
    print(output)

    #TODO: check if the -output arg is specified and save the output to a filie

if __name__ == '__main__':
    main()
