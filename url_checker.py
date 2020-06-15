from googlesearch import search
from urllib3 import PoolManager


def check_google_search_results(query: str):
    search_results = [
        search_result
        for search_result in search(query, tld="com", start=0, stop=9, pause=2)
    ]
    return [check_url_status(url) for url in search_results]


def check_url_status(url: str):
    http = PoolManager()
    r = http.request("GET", url)
    return r.status
