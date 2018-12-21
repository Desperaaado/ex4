from sys import argv
from sys import exit

lenth = len(argv)

def print_sentense(who='I', do='eat', what='apple'):
    print(f'Today {who} {do} {what}!!')

if '-h' in argv or '--help' in argv:
    print("""
        HELP:
            This program can show you a sentense on the basis of 
            three word which you inputed.
    """)
    exit(0)

try:
    if lenth == 4:
        script, who, do, what = argv
        print_sentense(who, do, what)
    elif lenth == 3:
        script, who, do = argv
        print_sentense(who, do)
    elif lenth ==2:
        script, who = argv
        print_sentense(who)
    else:
        print('Today I eat apple.')
        exit(1)
except ValueError:
    print('Today I eat apple!!')
    exit(0)




