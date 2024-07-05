"""Main entry point for PyCLI"""

import argparse


def head(f, n, c):
    return f, n, c


def wc(l):
    return l


def main():
    """Main entry point to the CLI"""
    parser = argparse.ArgumentParser(
        prog="pycli",
        description="A Python CLI that demonstrates many core Unix commands",
    )

    # Add subparser so we can do multiple commands
    # using the 'dest' is helpful to add a namespace to query on
    subparser = parser.add_subparsers(help="Sub-command help", dest="commands")

    # Head command
    head_parse = subparser.add_parser(name="head")
    head_parse.add_argument("file", type=str)
    head_parse.add_argument("-n", dest="n", type=int)
    head_parse.add_argument("-c", dest="c", type=int)
    head_parse.set_defaults(func=head)

    # WC command
    wc_parse = subparser.add_parser(name="wc")
    wc_parse.add_argument("-l", dest="operand", type=int)
    wc_parse.set_defaults(func=wc)

    # Gather up the args passed to us
    args = parser.parse_args()

    # Capture execution in a try block
    try:
        # Get the function call we'll pass this to
        func = args.func
        # Switch based on what command was provided for the subcommand
        if args.commands == "head":
            value = func(f=args.file, n=args.n, c=args.c)
            print(value)
    except:
        parser.error("Too few arguments")
    # print(head_parse.parse_args())


if __name__ == "__main__":
    main()
