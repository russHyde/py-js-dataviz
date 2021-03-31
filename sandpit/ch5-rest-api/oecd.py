"""
Script for REST-API access to data from OECD
"""

import requests

OECD_ROOT_URL = "http://stats.oecd.org/sdmx-json/data"


def make_oecd_request(dsname, dimensions, params=None, root_dir=OECD_ROOT_URL):
    """
    Make a URL for the OECD API and return a response
    """

    if not params:
        params = {}

    dim_args = ["+".join(d) for d in dimensions]
    dim_str = ".".join(dim_args)

    url = root_dir + "/" + dsname + "/" + dim_str + "/all"
    print("requesting URL: " + url)

    return requests.get(url, params=params)


if __name__ == "__main__":
    response = make_oecd_request(
        "QNA",
        (("USA", "AUS"), ("GDP", "B1_GE"), ("CUR", "VOBARSA"), ("Q")),
        {"startTime": "2009-Q1", "endTime": "2010-Q1"},
    )

    if response.status_code == 200:
        json = response.json()
        print(json.keys())
