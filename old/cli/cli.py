# CLI interface for hamframe

import argparse


# local constants

AVAILABLE_CONFIG_OPS = [ "import", "export" ]
# AVAILABLE_CONFIG_SECTIONS = ["clublog", "n0nbh", "qrz", "redis"]
AVAILABLE_CONFIG_SECTIONS = ["couchbase"]

# define a custom formatter to honor newlines in help text
# inspired by https://stackoverflow.com/questions/3853722/how-to-insert-newlines-on-argparse-help-text
# use the above URL for instructions on how to use this formatter since it's currently available but 
# not used in the code below.

class SmartFormatter(argparse.HelpFormatter):
    
    def _split_lines(self, text: str, width: int) -> list[str]:
        if text.startswith('R|'):
            return text[2:].splitlines()
        return super()._split_lines(text, width)



# define the arg parser

def parse_arguments():
    parser = argparse.ArgumentParser(description='Interact with hamframe',
                                    prog='hamframe-cli',
                                    add_help=True,
                                    formatter_class=SmartFormatter)

    # add optional flags

    parser.add_argument('--instance', type=str, help='instance name')
    parser.add_argument('--confdir', type=str, help='path to configuration files')
    parser.add_argument('--redis', type=str, help='Redis server')
    parser.add_argument('-v', '--verbose', action="store_true", help='be noisy')

    # create the commands we understand

    command_parsers = parser.add_subparsers(dest='command')

    # help
    help_parser = command_parsers.add_parser('help', help='produce this message or specify a command to produce help on')
    help_parser.add_argument('subcommand', nargs='*')

    # status
    status_parser = command_parsers.add_parser('status', help='report status')

    # config
    config_parser = command_parsers.add_parser('config', help='interact with configuration')
    config_parser.add_argument('subcommand', nargs='*')

    args = parser.parse_args()

    return parser, args



# command 'help' handler

def handle_help(parser, args):
    if args.subcommand:
        help_command = args.subcommand[0]
        match help_command:
            case 'config':
                print('\nInteract with configuration\n'
                      '\n'
                      'Requires\n'
                      '\t--instance and\n'
                      '\t--confdir or --redis\n'
                      '\n'
                      'Subcommands:\n'
                      '\n'
                      '\timport [section]\n'
                      '\texport [section]\n')
            case 'status':
                print('\nReports system status.\n'
                '\n'
                'Requires\n'
                '\t--instance and\n'
                '\t--confdir or --redis or both\n')
            case 'help':
                parser.print_help()
            case _:
                parser.print_help()
                print('\nERROR:\tcommand \'' + help_command + '\' not recognized.\n')
                exit(1)
    else:
        parser.print_help()
        print('\nFor help on specific commands, try:\n'
              '\n'
              '\thelp status\n')
    exit(0)



# command 'status' handler

def handle_status(parser, args):
    if args.instance and (args.confdir or args.redis):
        print('\nno status for you.\n') # FIXME: placebo until backend is alive
        exit(0)
    else:
        parser.print_help()
        print('\nERROR:\tmissing required arguments; check \'help status\'.\n')
        exit(1)



# command 'config' handler

def handle_config(parser, args):
    if not args.subcommand or len(args.subcommand) > 2:
        print('\nERROR:\tincorrect number of arguments; check \'help config\'.\n')
        exit(1)
    
    else:
        config_op = args.subcommand[0]
        if not config_op in AVAILABLE_CONFIG_OPS:
            print('\nERROR:\tcommand \'' + args.subcommand[0] + '\' not recognized.\n')
            exit(1)
        
        if (len(args.subcommand) == 2):
            config_section = args.subcommand[1]
            if not config_section in AVAILABLE_CONFIG_SECTIONS:
                print('ERROR:\tconfiguration section not recognized.')
                print('\tprovided: \'' + config_section + '\'')
                print('\tavailable:', str(AVAILABLE_CONFIG_SECTIONS))
                exit(1)
        else:
            config_section = ''
      
        match config_op:
            case 'import':
                print() # FIXME: placebo until backend is alive
            case 'export':
                print() # FIXME: placebo until backend is alive



# process the args

if __name__ == '__main__':
    parser, args = parse_arguments()

    if args.command == 'help':
        handle_help(parser, args)
    elif args.command == 'status':
        handle_status(parser, args)
    elif args.command == 'config':
        handle_config(parser, args)
    else:
        parser.print_help()
        exit(0)
