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
    # CSV = "data/nobel_winners_ds.csv"

    print(winners(DB))

    # Drop the existing table
    drop_winners_table(DB)

    # Show that the winners table is now empty
    print(winners(DB))

    # Remake the winners table using `dataset` syntax
    create_winners_table(DB)
    print(winners(DB))

    # Make a csv from the winners table using {dataset}
    #   - this no longer works, .freeze has been moved to {datafreeze} which is
    #   not under active development (hasn't been released in 4 years)
    #   - ? recommend using pandas.to_csv and pandas.read_sql_query
    # winner_set = DB["winners"].find()
    # dataset.freeze(winner_set, format="csv", filename=CSV)
