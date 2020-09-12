import re
import itertools


class Anonymize:

    def __init__(self):
        pass

    def get_hashtag_lists(self, list_post):

        regex = "#(\w+)"
        hashtag_lists = []

        for item in list_post:

            edge_media_to_caption = item['edge_media_to_caption']
            edges = edge_media_to_caption['edges']

            if len(edges) > 0:
                node = edges[0]['node']
                text = node['text']
                word_list = re.findall(regex, text)

                if len(word_list) > 0:
                    hashtag_lists.append(word_list)

        hashtag_list = list(itertools.chain.from_iterable(hashtag_lists))
        
        return hashtag_list
