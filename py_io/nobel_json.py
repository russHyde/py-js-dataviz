import json
import os

from nobel import NOBEL_WINNERS


def write_json(list_of_dicts, file_path):
    """
    Writes a list of dictionaries to a file
    """
    with open(file_path, "w") as file_writer:
        json.dump(list_of_dicts, file_writer)


def read_json(file_path):
    """
    Reads some data from a json file
    """
    with open(file_path) as file_reader:
        return json.load(file_reader)


if __name__ == "__main__":
    FILE = os.path.join("data", "nobel_winners.json")

    write_json(NOBEL_WINNERS, FILE)

    data = read_json(FILE)
    print(data)
