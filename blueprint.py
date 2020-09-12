from flask_swagger_ui import get_swaggerui_blueprint


class Schema:

    def __init__(self):
        pass

    def get_blueprint(self, url, api_url):

        SWAGGER_URL = url
        API_URL = api_url
        swaggerui_blueprint = get_swaggerui_blueprint(url, api_url)
        return swaggerui_blueprint
