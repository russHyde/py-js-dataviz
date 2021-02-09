import dataset

from nobel import NOBEL_WINNERS


def winners(db):
    wtable = db["winners"]
    _winners = wtable.find()
    return list(_winners)


def drop_winners_table(db):
    wtable = db["winners"]
    wtable.drop()


def create_winners_table(db):
    with db as transaction:
        for winner in NOBEL_WINNERS:
            transaction["winners"].insert(winner)


if __name__ == "__main__":
    URL = "sqlite:///data/nobel_prize.db"
    DB = dataset.connect(URL)

    print(winners(DB))

    # Drop the existing table
    drop_winners_table(DB)

    # Show that the winners table is now empty
    print(winners(DB))

    # Remake the winners table using `dataset` syntax
    create_winners_table(DB)
    print(winners(DB))
