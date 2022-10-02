"""
Loads the reviews, calculates the length of each review (in characters), and
saves the lengths to a file.
"""

import typer

app = typer.Typer()


@app.command()
def count_length(
    input_path: str = typer.Option(..., help="Path to the input file"),
    output_path: str = typer.Option(..., help="Path to the output file"),
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


if __name__ == "__main__":
    app()
