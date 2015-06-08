#!/usr/bin/env python3
import sys
import random

filler_map =  ['b', 'c', 'd', 'f', 'g', \
               'h', 'j', 'k', 'l', 'm', \
               'n', 'p', 'r', 's', 'w']

nouns = ['a', 'e', 'i', 'o', 'u']

def main():
    was_noun = (random.randint(0, 1) == 1)
    for x in range(0, random.randint(4, 14)):
        if was_noun:
            was_noun = False
            _tmp = filler_map[random.randint(0, len(filler_map) - 1)]
        else:
            was_noun = True
            _tmp = nouns[random.randint(0, len(nouns) - 1)]

        if x == 0:
            print(_tmp.upper(), end='')
        elif x > 4 and _tmp in ['x', 'y', 'z']:
            print(_tmp, end='')
            break
        else:
            print(_tmp, end='')

    # print an empty line
    print()

def error_exit(message=None, error=None):
    if message is not None:
        print(message)

    if error is not None:
        raise error

    print() # print empty line
    print("usage: {0} [argument <value>]".format(sys.argv[0]))
    sys.exit(1)

if __name__ == '__main__':
    args = dict(zip(sys.argv[1::2], sys.argv[2::2]))
    for argument, value in args.items():
        if '--times' == argument \
        or '-t' == argument:
            try:
                times = int(value)
            except ValueError:
                error_exit("The `{0}` argument was supplied with " \
                    "an invalid value.".format(argument))

            for x in range(0, times):
                main()
        else:
            error_exit("Script supplied with invalid argument `{0}` " \
                "is not defined".format(argument))
    else:
        main()
