"""Main entry point for PyCLI"""

import argparse
from .head import Head
from .wc import WC
import sys


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
    head_parse.add_argument("files", type=str, nargs="+")
    head_parse.add_argument("-n", dest="n", type=int)
    head_parse.add_argument("-c", dest="c", type=int)

    # WC command
    wc_parse = subparser.add_parser(name="wc")
    wc_parse.add_argument("files", type=str, nargs="*", default=sys.stdin)
    wc_parse.add_argument("-c", dest="c", action="store_true")
    wc_parse.add_argument("-l", dest="l", action="store_true")
    wc_parse.add_argument("-m", dest="m", action="store_true")
    wc_parse.add_argument("-w", dest="w", action="store_true")

    # Gather up the args passed to us
    args = parser.parse_args()

    # Capture execution in a try block
    try:
        # Get the function call we'll pass this to
        # Switch based on what command was provided for the subcommand
        if args.commands == "head":
            head = Head(args.files, args.n, args.c)
            if args.n:
                head.head("lines")
            if args.c:
                head.head("bytes")
        if args.commands == "wc":
            print(type(args.files))
            wc = WC(args.files, args.c, args.l, args.m, args.w)
            wc.wc()
    except Exception as e:
        print(e)
    # print(head_parse.parse_args())


if __name__ == "__main__":
    main()