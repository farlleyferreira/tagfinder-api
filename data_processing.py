import re
import math
import nltk
import requests
import itertools
import numpy as np

from nltk.corpus import stopwords
from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# nltk.download('punkt')
# nltk.download('stopwords')


class Processor:
    """
        Classe responsavel pelo processamento dos dados pertinentes ao projeto 
    """

    def __init__(self):
        pass

    def translate_number(self, unity):
        """
            Funçao responsavel por traduzir as unidades textuais do scraping feito no instagram

        Params:
            unity (string): unidade retornada pelo scraping das paginas do instagram

        Returns:
            value (float): retorna o fator multiplicativo referente a unidade proveniente do instagram
        """

        if unity == 'bi':
            return 1000000000

        elif unity == 'mi':
            return 1000000

        elif unity == 'mil':
            return 1000

        else:
            return 1

    def get_hashtag_rates(self, hashtag_text):
        """
            Funcao responsavel por realizar a limpeza e processar o resultado do scraping feito no instagram

        Params:
            hashtag_text (string): texto resultante do scraping feito no instagram

        Returns:
            post_rate (float): numero de citações da tag pesquisada
        """

        if hashtag_text:
            value = hashtag_text.split(' ')

            post_rate = float(value[0].replace(',', '.')) * \
                self.translate_number(value[1])

            return post_rate

        else:
            return 0

    def get_stopwords(self, language):
        """
            Funcao responsavel carregar a lista de stopwords para o processamento

        Params:
            language (string): idioma de busca das stopwords

        Returns:
            stopwords (list): lista de stopwords carregadas
        """

        stopwords = nltk.corpus.stopwords.words(language)
        stopwords.extend(['?', '.', ',', '(', ')', '!'])

        return stopwords

    def process_sentences(self, sentences):
        """
            Funcao responsavel por processar (limpar palavras indesejadas) as sentenças geradas a partir de um texto

        Args:
            sentences (list): lista de sentenças alvo

        Returns:
            cleaned_sentences (list): lista de sentenças processadas
        """

        cleaned_sentences = []
        stopwords = self.get_stopwords('portuguese')

        for sentence in sentences:

            tokenized_sentence = word_tokenize(sentence)

            clean_sentence = [
                token for token in tokenized_sentence if token not in stopwords
            ]

            cleaned_sentences.append(' '.join(clean_sentence))

        return cleaned_sentences

    def get_hashtags(self, sentences):
        """
            Funcao responsavel por encontrar as palavras chave em um texto

        Args:
            sentences (list): lista de sentenças alvo

        Returns:
            hashtags (list): lista de hashtags encontradas a partir de um conjunto de sentenças
        """

        terms_vectorized = TfidfVectorizer()
        terms_vectorized.fit_transform(sentences)
        terms = terms_vectorized.get_feature_names()

        sentence_scores = terms_vectorized.transform(sentences).toarray()
        scores = np.array(sentence_scores).ravel()

        data = list(zip(terms, scores))
        hashtags = [value for value, key in data if key > 0]

        return hashtags
