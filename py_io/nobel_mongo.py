from pymongo import MongoClient

from nobel import NOBEL_WINNERS

DB_NOBEL_PRIZE = "nobel_prize"
COLL_WINNERS = "winners"


def get_mongo_database(
    db_name, host="localhost", port=27017, username=None, password=None
):
    """
    Get named database from MongoDB with/out authentication
    """
    # make Mongo connection with/out authentication
    if username and password:
        mongo_uri = f"mongodb://{username}:{password}@{host}/{db_name}"
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db_name]


def mongo_coll_to_dicts(db_name="test", coll_name="test", query={}, del_id=True, **kw):
    """
    Note that the book uses arg dbname and collname; we changed this for
    consistency with get_mongo_database
    """
    my_db = get_mongo_database(db_name, **kw)
    res = list(my_db[coll_name].find(query))

    if del_id:
        for entry in res:
            entry.pop("_id")

    return res


def summary(coll):
    print("\n\nThe Mongo collection:\n")
    print(coll)

    print("\n\nThe modified python collection:\n")
    print(NOBEL_WINNERS)

    print("\n\nChemistry winners:\n")
    res = coll.find({"category": "Chemistry"})
    print(list(res))

    print("\n\nWinners after 1930\n")
    res = coll.find({"year": {"$gt": 1930}})
    print(list(res))

    print("\n\nWinners who are either female or who won after 1930\n")
    res = coll.find({"$or": [{"year": {"$gt": 1930}}, {"sex": "female"}]})
    print(list(res))


if __name__ == "__main__":
    client = MongoClient()
    db = get_mongo_database(DB_NOBEL_PRIZE)
    coll = db[COLL_WINNERS]

    # start this script from an empty database
    coll.drop()

    coll.insert_many(NOBEL_WINNERS)

    summary(coll)

    print("\n\nThe Mongo collection converted back to python dicts\n")
    print(mongo_coll_to_dicts(DB_NOBEL_PRIZE, COLL_WINNERS))
