# accepts parameters as commands

import argparse

parser = argparse.ArgumentParser(description="parse what we're given from docker run")
parser.add_argument('command', type=str, help="CLI command to be executed")
parser.add_argument('--file', type=str, help="filename to pass to command")

args = parser.parse_args()

print(args.command)
if args.file:
    print(args.file)
