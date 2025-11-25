"""googlesearch is a Python library for searching Google, easily."""
from time import sleep
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSearchError(Exception):
    pass


class SearchResult:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    def __repr__(self):
        return f"SearchResult(url={self.url}, title={self.title}, description={self.description})"


def search(term, num_results=10, lang="en", advanced=False, sleep_interval=0, api_key=None, cse_id=None, region=None, safe="active"):
    """Search the Google search engine using the Custom Search API"""

    if not api_key:
        try:
            with open("apikey", "r") as f:
                api_key = f.read().strip()
        except FileNotFoundError:
            raise ValueError("API key not provided and 'apikey' file not found.")

    if not cse_id:
        # To get a Custom Search Engine ID, visit:
        # https://programmablesearch.google.com/controlpanel/all
        raise ValueError("Custom Search Engine ID (cse_id) must be provided.")

    if num_results > 100:
        print("Warning: The Google Custom Search API is limited to 100 results.")
        num_results = 100

    # Build the service object
    service = build("customsearch", "v1", developerKey=api_key)

    # The API is limited to 10 results per request.
    # We need to make multiple requests to get more than 10 results.
    for start in range(0, num_results, 10):
        # The API allows a maximum of 10 results per request.
        num = min(num_results - start, 10)
        start_index = start + 1 # API is 1-based

        try:
            res = service.cse().list(
                q=term,
                cx=cse_id,
                num=num,
                hl=lang,
                gl=region,
                safe=safe,
                start=start_index
            ).execute()
        except HttpError as e:
            raise GoogleSearchError(f"Google API returned an error: {e}")

        items = res.get('items', [])
        if not items:
            break # No more results

        for item in items:
            link = item.get('link')

            if advanced:
                title = item.get('title')
                description = item.get('snippet')
                result = SearchResult(link, title, description)
            else:
                result = link

            yield result

        if len(items) < 10:
            break # No more results to fetch

        if sleep_interval > 0:
            sleep(sleep_interval)
