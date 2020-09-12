class Forge:
    """
    Classe responsavel por emular um cabeçalho valido de requisicao
    """

    def __init__(self, token):
        self.token = token

    def custom_headers(self):
        """[summary]

        Returns:
            header (object): retorna um cabecalho valido para realizar requisicoes ao instagram
        """

        header = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'cookie': 'sessionid={0};'.format(self.token)
        }
        return header
