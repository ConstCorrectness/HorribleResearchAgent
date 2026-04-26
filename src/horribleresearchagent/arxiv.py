import urllib.parse
import urllib.request

"""
https://export.arxiv.org/api/{method}?{parameters}
    
    query:
        search_query: str
        id_list: list[str]
        start: int
        max_results: int = 10
    Ex:
        https://export.arxiv.org/api/query?page=1&limit=10&search_results=alice
"""


ARXIV_API_URL = 'https://export.arxiv.org/api'



def query_arxiv(search_query: str, max_results: int = 10):
    """ 
        Queries `max_results` articles on arxiv for `search_query`
    """

    query_parameters = {
        'search_query': search_query,
        'max_results': max_results
    }

    url = f'{ARXIV_API_URL}/query?{urllib.parse.urlencode(query_parameters)}'
    print(f'url = {url}')
    with urllib.request.urlopen(url) as response:
        data = response.read()
        data = data.decode('utf-8')

        print(data)








if __name__ == '__main__':
    query_arxiv('agentic ai')