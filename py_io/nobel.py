"""
Target list of nobel prize winners, passed between different storage formats
"""

import os


def write_csv(my_dict, file_path):
    """
    Assumes the same keys are present in each element of my_dict
    """

    cols = list(my_dict[0].keys())
    cols.sort()

    with open(file_path, "w") as file_writer:
        file_writer.write(",".join(cols) + "\n")

        for row_dict in my_dict:
            row = [str(row_dict[col]) for col in cols]
            file_writer.write(",".join(row) + "\n")


def cat(file_path):
    """
    print the contents of a file to the console
    """
    with open(file_path) as file_reader:
        for line in file_reader.readlines():
            print(line.strip())


nobel_winners = [
    {
        "category": "Physics",
        "name": "Albert Einstein",
        "nationality": "Swiss",
        "sex": "male",
        "year": 1921,
    },
    {
        "category": "Physics",
        "name": "Paul Dirac",
        "nationality": "British",
        "sex": "male",
        "year": 1933,
    },
    {
        "category": "Chemistry",
        "name": "Marie Curie",
        "nationality": "Polish",
        "sex": "female",
        "year": 1911,
    },
]

if __name__ == "__main__":
    FILE = os.path.join("data", "nobel_winners.csv")

    write_csv(nobel_winners, FILE)

    cat(FILE)
