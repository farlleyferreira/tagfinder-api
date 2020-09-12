import time
import random

from data_store import Data
from data_sanitize import Anonymize
from data_analysis import Analyzers
from data_processing import Processor
from instagram_scraping import Crawling


data = Data()
crawling = Crawling()
anonymize = Anonymize()
analyzers = Analyzers()
processor = Processor()

target = 'instagood'

hashtag_response = data.get_hashtag(target)

if hashtag_response != "1":

    list_of_posts = crawling.get_post_list(target)
    list_of_hashtags = anonymize.get_hashtag_lists(list_of_posts)
    list_of_hashtags_unique = analyzers.get_hashtag_frquency(list_of_hashtags)
    list_of_hashtags_unique = random.sample(list_of_hashtags_unique, 100)
    counter = 0
    while counter < len(list_of_hashtags_unique):

        if (counter % 5) == 0:
            time.sleep(3)

        hashtag_rates = crawling.get_hashtag_rates(
            list_of_hashtags_unique[counter]['tag']
        )
        list_of_hashtags_unique[counter]['rates'] = processor.get_hashtag_rates(
            hashtag_rates
        )

        status = data.add_hashtag(list_of_hashtags_unique[counter])
        print('status: ', status, counter, 'of', len(list_of_hashtags_unique))
        counter += 1

    print(list_of_hashtags_unique)

else:
    hashtag_response
