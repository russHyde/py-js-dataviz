"""
Obtain data via the RESTful restcountries.eu API
"""

import requests
from nobel_mongo import get_mongo_database


REST_EU_ROOT_URL = "http://restcountries.eu/rest/v1"


def rest_country_request(field="all", name=None, params=None):
    """
    Make a URL for the `restcountries.eu` API and return a response
    """

    headers = {"User-Agent": "Mozilla/5.0"}

    if not params:
        params = {}

    if field == "all":
        return requests.get(REST_EU_ROOT_URL + "/all")

    url = f"{REST_EU_ROOT_URL}/{field}/{name}"
    print(f"Requesting: {url}")

    response = requests.get(url, params=params, headers=headers)

    if not response.status_code == 200:
        raise Exception(
            "Request failed with status code: {}".format(str(response.status_code))
        )

    return response


if __name__ == "__main__":
    # add the country data to the mongo database
    DB_NOBEL = get_mongo_database("nobel_prize")
    COL = DB_NOBEL["country_data"] # country data collection
    COL.drop() # add the data to an empty table

    # get all the RESTful country-data
    RESPONSE = rest_country_request()
    # insert the JSON-objects straight to our collection
    COL.insert_many(RESPONSE.json())

    res = COL.find({"currencies": {"$in": ["USD"]}})
    print(list(res))
