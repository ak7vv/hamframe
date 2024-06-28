# CLI interface for hamframe

import argparse


# define a formatter to honor newlines in help text
# https://stackoverflow.com/questions/3853722/how-to-insert-newlines-on-argparse-help-text

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

    return parser, parser.parse_args()


# help handler

def handle_help(parser, args):
    if args.subcommand:
        match args.subcommand[0]:
            case 'status':
                print('\nReports the system status.\n'
                '\n'
                'Requires\n'
                '\t--instance and\n'
                '\t--confdir or --redis\n')
            case 'help':
                parser.print_help()
            case _:
                parser.print_help()
                print('\nERROR: command not recognized.\n')
                exit(1)
    else:
        print('\nProvides help on specific commands.\n'
              '\n'
              'Example:\n'
              '\thelp status\n')
    exit(0)


# status handler

def handle_status(parser, args):
    if args.instance and (args.confdir or args.redis):
        print('\nno status for you.\n')
        exit(0)
    else:
        parser.print_help()
        print('\nERROR: missing required arguments; check \'help status\'.\n')
        exit(1)


# config handler

def handle_config(parser, args):
    if not args.subcommand or len(args.subcommand) > 2:
        print('\nERROR: incorrect number of arguments; check \'help config\'.\n')
        exit(1)
    else:
        if args.subcommand[0] != ('import' or 'export'):
            print('\nERROR: command not recognized.\n')
            exit(1)
        else:
            config_op = args.subcommand[0]
        if (len(args.subcommand) == 2):
            config_section = args.subcommand[1]
            available_config_sections = ["clublog", "n0nbh", "qrz", "redis"]
            if not config_section in available_config_sections:
                print('ERROR: configuration section not recognized')
                exit(1)
        else:
            config_section = ''
      
        match config_op:
            case 'import':
                print()
            case 'export':
                print()



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
        print('\nRefer to the documentation for a complete reference.\n')
