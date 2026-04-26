import pytest
import json

from urllib.parse import urlencode
from urllib.request import urlopen, Request

from horribleresearchagent.arxiv import ARXIV_API_URL


def test_url():
    """
        ARXIV_API_URL = https://export.arxiv.org/api
    """

    query_string_parameters = {
        'search_query': 'all:electron'
    }

    s = f'{ARXIV_API_URL}/query?{urlencode(query_string_parameters)}'

    assert s == 'https://export.arxiv.org/api/query?search_query=all%3Aelectron'     # colon (:) gets percent-encoded as %3A



def test_get():
    """
        HTTP GET 
    """
    parameters = {
        'search_query': 'all:DeepSeek V4',
        'start': 0,
        'max_results': 1
    }

    full_url = f'{ARXIV_API_URL}/query?{urlencode(parameters)}'

    with urlopen(full_url) as response:
        html = response.read().decode('utf-8')
        print(f'GET status: {response.status}')
        print(html[:200])

    

def test_post():
    """
        HTTP POST
    """
    parameters = {
        'search_query': 'all:Agentic AI',
        'max_results': 1
    }

    full_url = f'{ARXIV_API_URL}/query'
    print(f'full_url = {full_url}')

    # POST needs to percent-encode and convert to UTF-8 bytes body data:
    data = urlencode(parameters)
    data = data.encode('utf-8')

    req = Request(full_url, data=data, headers={
        'Content-Type': 'application/x-www-form-urlencoded'
    })

    with urlopen(req) as response:
        result = response.read().decode('utf-8')
        print(f'POST status: {response.status}')
        print(result[:500])

