from datetime import datetime
class Pessoa:

    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))


    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar de boca cheia.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print(f'{self.nome} já não estava falando.')
            return

        print(f'{self.nome} parou de falar.')

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return  # A palavra return não deixa nada abaixo ser executado

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def pararComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    @classmethod
    def porAnoDeNascimento(cls, nome, anoNascimento):
        idade = cls.anoAtual - anoNascimento
        return cls(nome, idade)

    def getAnoNascimento(self):
        return self.anoAtual - self.idade

#p1 = Pessoa.porAnoDeNascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)
print(p1.nome, p1.idade)
print(p1.getAnoNascimento())