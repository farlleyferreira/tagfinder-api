
import time
import json
import requests

from utils.cookie_forge import Forge
from bs4 import BeautifulSoup


class Crawling:
    """
    Classe responsavel pela raspagem das paginas do instagram
    """

    def __init__(self):
        pass

    def get_post_list(self, tag_target):
        """
            Sera abordada em artigos futuros

        Args:
            tag_target ([type]): [description]

        Returns:
            [type]: [description]
        """

        page_number = 0
        end_cursor = ''
        post_list = []

        config = json.load(open('configs/crawler.json'))

        page_count = config['page_number']
        base_url = config['posts_base_url']
        token = config['token']

        forge = Forge(token)
        custom_header = forge.custom_headers()

        while page_number < page_count:

            url = base_url.format(tag_target, end_cursor)
            data = requests.get(url, headers=custom_header).json()

            graphql = data['graphql']
            hashtag = graphql['hashtag']
            edge_hashtag_to_media = hashtag['edge_hashtag_to_media']

            page_info = edge_hashtag_to_media['page_info']
            end_cursor = page_info['end_cursor']

            edges = edge_hashtag_to_media['edges']

            for item in edges:
                post_list.append(item['node'])

            page_number += 1
            time.sleep(2)

        return post_list

    def get_hashtag_rates(self, tag_target):
        """
            Funcao responsavel por realizar um scraping nas paginas do instagram e identificar o número de citacoes para uma tag

        Params:
            tag_target (string): tag alvo

        Returns:
            data (string): texto referente ao numero de citacoes
        """

        config = json.load(open('configs/crawler.json'))

        token = config['token']
        base_url = config['hashtag_base_url']

        forge = Forge(token)
        custom_header = forge.custom_headers()

        url = base_url.format(tag_target)
        page = requests.get(url, headers=custom_header)
        soup = BeautifulSoup(page.content, 'html.parser')
        meta = soup.find('meta', attrs={'name': 'description'})

        content = meta.attrs['content'].split('-')
        data = content[0]
        return data
