import time

from data_processing import Processor
from instagram_scraping import Crawling
from nltk import sent_tokenize


class Process:
    """
        Classe responsavel pelo processamento das hashtags 
    """

    def __init__(self):
        pass

    def get_hashtag_rates(self, hashtag_list):
        """
            Funçao que implementa o metodo de scraping de palavras chave no instagram

        Params:
            hashtag_list (list): recebe uma lista de tags para pesquisar

        Returns:
            hashtag_rates_list (list): retorna uma lista contendo as palavras chave e, numero de citações para cada palavra chave encontradas pelo algoritmo
        """

        crawling = Crawling()
        processor = Processor()
        hashtag_rates_list = []

        for hashtag in hashtag_list:

            hashtag_rate_output = crawling.get_hashtag_rates(hashtag)
            hashtag_rate = processor.get_hashtag_rates(hashtag_rate_output)
            hashtag_rates_list.append(
                {'tag': hashtag, 'hits': 0, 'rates': hashtag_rate}
            )
            time.sleep(1.5)

        return hashtag_rates_list

    def get_hashtags(self, text_corpus):
        """
            Funçao que implementa o metodo de busca de palavras chave em um texto, a partir do metodo term frequency–inverse document frequency

        Params:
            text_corpus (string): recebe o texto desejado para realizar a busca de palavras chave

        Returns:
            hashtag_list (list): retorna uma lista contendo as palavras chave, encontradas pelo algoritmo
        """

        processor = Processor()
        sentences = sent_tokenize(text_corpus)
        cleaned_sentences = processor.process_sentences(sentences)
        hashtag_list = processor.get_hashtags(cleaned_sentences)

        return hashtag_list
