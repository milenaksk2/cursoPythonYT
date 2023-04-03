class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco  - (self.preco * (percentual/100))

    # Getter
    @property
    def nome(self):
        return self.nome

    # Setter
    @nome.setter()
    def nome(self, nome):
        self._nome = nome.title() #title é para armazenar valor apenas com a primeira letra maiuscula

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', '')) #transformando str em float

        self._preco = valor;

