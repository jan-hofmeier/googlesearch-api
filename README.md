# googlesearch
googlesearch is a Python library for searching Google, easily. googlesearch uses the google-api-python-client.

## Installation
To install, run the following command:
```bash
python3 -m pip install googlesearch-python
```

## Usage
To get results for a search term, you must first provide your credentials.

You will need an API key and a Custom Search Engine ID.
- To get an API key, visit: https://developers.google.com/custom-search/v1/overview#api_key
- To get a Custom Search Engine ID, visit: https://programmablesearchengine.google.com/controlpanel/all?hl=de

Set your credentials using the `set_api_key` and `set_cse_id` functions. These only need to be called once per session.

```python
from googlesearch import search, set_api_key, set_cse_id

# Set your credentials
set_api_key("YOUR_API_KEY")
set_cse_id("YOUR_CSE_ID")

# Now you can perform searches
results = search("Google")
```

Alternatively, you can place your API key in a file named `apikey` in the working directory, and it will be loaded automatically. You will still need to set the CSE ID.

## Additional options
googlesearch supports a few additional options. By default, googlesearch returns 10 results. This can be changed. To get 100 results on Google for example, run the following program.
```python
from googlesearch import search, set_api_key, set_cse_id

set_api_key("YOUR_API_KEY")
set_cse_id("YOUR_CSE_ID")

search("Google", num_results=100)
```
In addition, you can change the language google searches in. For example, to get results in French run the following program:
```python
from googlesearch import search, set_api_key, set_cse_id

set_api_key("YOUR_API_KEY")
set_cse_id("YOUR_CSE_ID")

search("Google", lang="fr")
```
To extract more information, such as the description or the result URL, use an advanced search:
```python
from googlesearch import search, set_api_key, set_cse_id

set_api_key("YOUR_API_KEY")
set_cse_id("YOUR_CSE_ID")

search("Google", advanced=True)
# Returns a generator of SearchResult objects
# Properties:
# - title
# - url
# - description
```
If requesting more than 10 results, googlesearch will send multiple requests to go through the pages. To increase the time between these requests, use `sleep_interval`:
```python
from googlesearch import search, set_api_key, set_cse_id

set_api_key("YOUR_API_KEY")
set_cse_id("YOUR_CSE_ID")

search("Google", sleep_interval=5, num_results=20)
```
