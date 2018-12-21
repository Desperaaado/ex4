import argparse
from textwrap import dedent

def print_sentense(who, do, what):
    print(f'Today {who} {do} {what}!!')

def print_fancy_sentense(who, do, what):
    print(f'Today~{who}~{do}~{what}!!')

parser = argparse.ArgumentParser(description=
    dedent("""This program can show you a sentense 
              on the basis of three word which you inputed.""")
)

parser.add_argument(
    '-f', '--fancy', action='store_true',
    help='Print fancy sentense.'
)
parser.add_argument('who', default='I', nargs='?')
parser.add_argument('do', default='eat', nargs='?')
parser.add_argument('what', default='apple', nargs='?')
args = parser.parse_args()

if not args.fancy:
    print_sentense(args.who, args.do, args.what)
else:
    print_fancy_sentense(args.who, args.do, args.what)