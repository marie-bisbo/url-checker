from googlesearch import search

query = "Brainlabs Digital"

for search_result in search(query, tld="com", start=0, stop=9, pause=2):
    print(search_result)
