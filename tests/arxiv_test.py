import pytest
import json

from urllib.parse import urlencode

from horribleresearchagent import arxiv


def test_url():
    """
        ARXIV_API_URL = http://export.arxiv.org/api/{method}?{parameters}
    """

    query_string_parameters = {
        'search_query': 'all:electron'
    }

    s = arxiv.ARXIV_API_URL.format(method='query', parameters=urlencode(query_string_parameters))

    assert s == 'http://export.arxiv.org/api/query?search_query=all%3Aelectron'

