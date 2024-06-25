import argparse

import userpath.core


class CLIArgs:
    command: str
    path: str


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    check_path_parser = subparsers.add_parser("check")
    check_path_parser.add_argument("path")

    append_parser = subparsers.add_parser("append")
    append_parser.add_argument("path")

    args = parser.parse_args(namespace=CLIArgs)
    if args.command == "check":
        if not userpath.in_current_path(args.path):
            raise SystemExit(1)

    elif args.command == "append":
        if not userpath.in_current_path(args.path):
            success = userpath.append(args.path)
            if not success:
                raise SystemExit(1)
