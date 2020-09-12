from tinydb import TinyDB, Query


class Data:

    def __init__(self):
        pass

    def add_hashtag(self, hashtag_object):

        Hashtag = Query()
        database = TinyDB('database/db.json')

        has_register = database.search(Hashtag.tag == hashtag_object['tag'])

        if has_register == hashtag_object:
            return 200, 'up to date'

        elif not has_register:
            database.insert(hashtag_object)
            return 201

        else:
            database.update(hashtag_object)
            return 200, 'up to date'

    def get_hashtag(self, hashtag):

        Hashtag = Query()
        database = TinyDB('database/db.json')
        has_register = database.search(Hashtag.tag == hashtag)

        return has_register
