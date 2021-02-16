import concurrent.futures

from googlesearch import search
from urllib3 import PoolManager


def check_google_search_results(query: str, number_of_results: int) -> list:
    search_results_urls = [
        search_result
        for search_result in search(
            query, tld="com", start=0, stop=number_of_results, pause=2
        )
    ]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(check_url_status, url) for url in search_results_urls
        ]
    return [future.result() for future in futures]


def check_url_status(url: str):
    http = PoolManager()
    request = http.request("GET", url)
    return request.status


print(check_google_search_results("Harry Potter", 10))
