
import argparse
from another_main import start_swap
import roop.globals


if __name__ == "__main__":

    program = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=100))

    roop.globals.frame_processors = ['face_swapper', 'face_enhancer']

    program.add_argument("--source_paths", nargs="+", required=True)
    program.add_argument("--target_paths", nargs="+", required=True)
    program.add_argument("--results", nargs="+", required=True)

    roop.globals.startup_args = program.parse_args()

    args = program.parse_args()

    start_swap(args.source_paths, args.target_paths, args.results)