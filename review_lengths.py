"""
Loads the reviews, calculates the length of each review (in characters), and
saves the lengths to a file.
"""

import argparse

def count_length(
    input_path: str,
    output_path: str
):
    """
    Loads the reviews, calculates the length of each review (in characters),
    and saves the lengths to a file.
    """

    with open(input_path, "r") as input_file:
        with open(output_path, "w") as output_file:
            output_file.write("length\n")

            for line in input_file:
                length = len(line)
                output_file.write(f"{str(length)}\n")

args = argparse.ArgumentParser()
args.add_argument("--input_path", type=str, required=True)
args.add_argument("--output_path", type=str, required=True)


if __name__ == "__main__":
    args = args.parse_args()
    count_length(args.input_path, args.output_path)

