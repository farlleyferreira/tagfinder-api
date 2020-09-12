

class Analyzers:

    def __init__(self):
        pass

    def get_hashtag_frquency(self, hashtag_list):

        hashtag_list_unique = set(hashtag_list)
        hashtag_ranking = []
        
        for hashtag_unique in hashtag_list_unique:
            counter = 0
            
            for hashtag in hashtag_list:    
                if hashtag_unique == hashtag:
                    counter += 1  
            
            hashtag_ranking.append({'tag': hashtag_unique, 'hits': counter, 'rates': hashtag_unique})
            
        hashtag_ranking = sorted(hashtag_ranking, key = lambda i: i['hits'], reverse=True)

        return hashtag_ranking

        