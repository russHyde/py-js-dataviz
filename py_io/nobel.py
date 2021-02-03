"""
Target list of nobel prize winners, passed between different storage formats
"""

import os
import csv


def write_csv(my_dict, file_path):
    """
    Assumes the same keys are present in each element of my_dict
    """

    fieldnames = list(my_dict[0].keys())
    fieldnames.sort()

    with open(file_path, "w") as file_writer:
        csv_writer = csv.DictWriter(file_writer, fieldnames=fieldnames)
        csv_writer.writeheader()
        for entry in my_dict:
            csv_writer.writerow(entry)


def cat_csv(file_path):
    """
    print the contents of a .csv file to the console
    """
    with open(file_path) as file_reader:
        csv_reader = csv.reader(file_reader)
        for row in csv_reader:
            # row is a list of values
            print(",".join(row))


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

    cat_csv(FILE)
