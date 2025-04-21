import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "log_files",
    nargs="+",
)
parser.add_argument(
    "--report",
    required=True,
    choices=['handlers']
    )


def get_args():
    return parser.parse_args()
