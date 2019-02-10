import typing
import requests
import json

from realestate_scraper.schematics import Search


def paged_results(query: Search, page_size=100) -> typing.Generator[dict, None, None]:
    BASE_URL = 'https://services.realestate.com.au/services/listings/search'

    _query = query.to_primitive()
    _query['pageSize'] = str(page_size)

    params = {'query': json.dumps(_query)}

    next_url = None
    more_pages = True
    while more_pages:
        if next_url:
            r = requests.get(next_url)
        else:
            r = requests.get(BASE_URL, params=params)
        json_data = r.json()

        yield json_data

        if not json_data['_links']['next']:
            more_pages = False
        else:
            next_url = json_data['_links']['next']['href']


# for page in paged_results():
#     print(page)
#
# page_data = [page for page in paged_results()]
