"""Main entry point for PyCLI"""

import argparse
from .head import Head
from .wc import WC
from .cat import Cat
from .cut import Cut
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

    # head command
    head_parse = subparser.add_parser(name="head")
    head_parse.add_argument("files", type=str, nargs="+")
    head_parse.add_argument("-n", dest="n", type=int)
    head_parse.add_argument("-c", dest="c", type=int)

    # wc command
    wc_parse = subparser.add_parser(name="wc")
    wc_parse.add_argument("files", type=str, nargs="*", default=sys.stdin)
    wc_parse.add_argument("-c", dest="c", action="store_true")
    wc_parse.add_argument("-l", dest="l", action="store_true")
    wc_parse.add_argument("-m", dest="m", action="store_true")
    wc_parse.add_argument("-w", dest="w", action="store_true")

    # cat command
    wc_parse = subparser.add_parser(name="cat")
    wc_parse.add_argument("files", type=str, nargs="*", default=sys.stdin)
    wc_parse.add_argument("-n", dest="n", action="store_true")
    wc_parse.add_argument("-b", dest="b", action="store_true")

    # cat command
    cut_parse = subparser.add_parser(name="cut")
    cut_parse.add_argument("files", type=str, nargs="*", default=sys.stdin)
    cut_parse.add_argument("-f", required=True, dest="f", type=str)
    cut_parse.add_argument("-d", dest="d", type=str, default="\t")

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
            wc = WC(args.files, args.c, args.l, args.m, args.w)
            wc.wc()
        if args.commands == "cat":
            if (
                isinstance(args.files, list)
                and len(args.files) == 1
                and args.files[0] == "-"
            ):
                args.files = sys.stdin
            cat = Cat(args.files, args.n, args.b)
            cat.cat()
        if args.commands == "cut":

            if (
                isinstance(args.files, list)
                and len(args.files) == 1
                and args.files[0] == "-"
            ):
                args.files = sys.stdin
            cut = Cut(args.files, args.f, args.d)
            cut.cut()
    except Exception as e:
        print(e)
    # print(head_parse.parse_args())


if __name__ == "__main__":
    main()
