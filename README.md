# googlesearch
googlesearch is a Python library for searching Google, easily. googlesearch uses the google-api-python-client.

## Installation
To install, run the following command:
```bash
python3 -m pip install googlesearch-python
```

## Usage
To get results for a search term, simply use the search function in googlesearch. For example, to get results for "Google" in Google, just run the following program:
```python
from googlesearch import search
# You will need an API key and a Custom Search Engine ID.
# To get an API key, visit: https://developers.google.com/custom-search/v1/overview#api_key
# To get a Custom Search Engine ID, visit: https://programmablesearch.google.com/controlpanel/all
search("Google", api_key="YOUR_API_KEY", cse_id="YOUR_CSE_ID")
```

You can also place your API key in a file named `apikey` in the same directory.

## Additional options
googlesearch supports a few additional options. By default, googlesearch returns 10 results. This can be changed. To get a 100 results on Google for example, run the following program.
```python
from googlesearch import search
search("Google", num_results=100, api_key="YOUR_API_KEY", cse_id="YOUR_CSE_ID")
```
In addition, you can change the language google searches in. For example, to get results in French run the following program:
```python
from googlesearch import search
search("Google", lang="fr", api_key="YOUR_API_KEY", cse_id="YOUR_CSE_ID")
```
To extract more information, such as the description or the result URL, use an advanced search:
```python
from googlesearch import search
search("Google", advanced=True, api_key="YOUR_API_KEY", cse_id="YOUR_CSE_ID")
# Returns a list of SearchResult
# Properties:
# - title
# - url
# - description
```
If requesting more than 10 results, googlesearch will send multiple requests to go through the pages. To increase the time between these requests, use `sleep_interval`:
```python
from googlesearch import search
search("Google", sleep_interval=5, num_results=20, api_key="YOUR_API_KEY", cse_id="YOUR_CSE_ID")
```
