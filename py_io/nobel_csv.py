"""
Target list of nobel prize winners, passed between different storage formats
"""

import os
import csv

from nobel import NOBEL_WINNERS


def write_csv(list_of_dicts, file_path):
    """
    Assumes the same keys are present in each element of list_of_dicts
    """

    fieldnames = list(list_of_dicts[0].keys())
    fieldnames.sort()

    with open(file_path, "w") as file_writer:
        csv_writer = csv.DictWriter(file_writer, fieldnames=fieldnames)
        csv_writer.writeheader()
        for entry in list_of_dicts:
            csv_writer.writerow(entry)


def read_csv(file_path):
    """
    return the contents of a .csv as a list of dictionaries
    """
    with open(file_path) as file_reader:
        csv_reader = csv.DictReader(file_reader)
        contents = list(csv_reader)

    return contents


def cat_csv(file_path):
    """
    print the contents of a .csv file to the console
    """
    with open(file_path) as file_reader:
        csv_reader = csv.reader(file_reader)
        for row in csv_reader:
            # row is a list of values
            print(",".join(row))


def format_winners_dict(my_dict):
    """
    convert numeric columns of a winner-dictionary
    """
    my_dict["year"] = int(my_dict["year"])
    return my_dict


if __name__ == "__main__":
    FILE = os.path.join("data", "nobel_winners.csv")

    write_csv(NOBEL_WINNERS, FILE)

    imported = read_csv(FILE)
    formatted = [format_winners_dict(winner) for winner in imported]
    print(formatted)
