# accepts parameters as commands

import argparse

# define a formatter to honor newlines in help text
# https://stackoverflow.com/questions/3853722/how-to-insert-newlines-on-argparse-help-text

class SmartFormatter(argparse.HelpFormatter):
    
    def _split_lines(self, text: str, width: int) -> list[str]:
        if text.startswith('R|'):
            return text[2:].splitlines()
        return super()._split_lines(text, width)

parser = argparse.ArgumentParser(description='Interact with hamframe',
                                 prog='hamframe-cli',
                                 add_help=True,
#                                 usage='%(prog)s [command | -h | --help]',
                                 epilog='Refer to the documentation for a complete reference.',
                                 formatter_class=SmartFormatter)

# add optional flags

parser.add_argument('--instance',
                    type=str,
                    help='instance name')

parser.add_argument('--confdir',
                    type=str,
                    help='path to configuration files')

parser.add_argument('--redis',
                    type=str,
                    help='Redis server')

parser.add_argument('-v', '--verbose',
                    action="store_true",
                    help='be noisy')

# create the commands we understand

group = parser.add_mutually_exclusive_group(required=False)
group.add_argument('help', help='produce this message', nargs='*', default=[])
group.add_argument('status',help='report status', nargs='?', default=[])

# process the args

args = parser.parse_args()

print(args)

# did we get any command args?  
# Note: For some reason args.help is the only thing ever populated and args.status etc never is.

if len(args.help) > 0:  # yes
    match args.help[0]:
        case 'help':
            match args.help[1]:
                case 'status':
                    print('Reports the system status.\n'
                        '\n'
                        'Requires --instance and either --confdir or --redis to be present')
                case _:
                    parser.print_help()
        case 'status':
            if args.instance and (args.confdir or args.redis):
                print('no status.')
            else:
                print('Missing required arguments.')
        case _:
            parser.print_help()
else: # no
    parser.print_help()

