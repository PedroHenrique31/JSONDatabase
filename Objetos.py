from datetime import date  # Certifique-se de importar o tipo de dado Date
from abc import ABC, abstractmethod

"""
    Classe de objetos do programa
    O presente arquivo amarazena as classes de objetos que lidaremos nesse trabalho
    esses objetos são posteriormente serializados e salvos num arquivo json.
"""

class Objeto(ABC):

    @abstractmethod
    def to_dict(self):
        pass

class Endereco(Objeto):
    def __init__(self, endereco, bairro, cidade, uf, cep):
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

    def to_dict(self):
        return {
            "endereco": self.endereco,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "uf": self.uf,
            "cep": self.cep
        }

class Telefone(Objeto):
    def __init__(self,telefone,ddd):
        self.telefone = telefone
        self.ddd = ddd
    def __init__(self, telefone, ddd, notas):
        self.telefone = telefone
        self.ddd = ddd
        self.notas = notas

    def to_dict(self):
        return {
            "telefone": self.telefone,
            "ddd": self.ddd,
            "notas": self.notas
        }

class Segurado(Objeto):
    def __init__(self, nome, cpf, rg, data_nascimento: date):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        self.telefones = []  # Inicializa uma lista de telefones
        self.apolices = []  # Inicializa uma lista de apólices

    def addApolice(self, apolice):
        """Adiciona uma apólice ao segurado"""
        if self.apolices is None:
            self.apolices = []
        self.apolices.append(apolice)

    def addTelefone(self, telefone):
        """Adiciona um telefone ao segurado"""
        if self.telefones is None:
            self.telefones = []
        self.telefones.append(telefone)

    def addEndereco(self):
        pass

    def addEmail(self):
        pass

    def to_dict(self):
        """Converte o objeto Segurado em um dicionário, incluindo telefones e apólices"""
        obj = {
            "nome": self.nome,
            "cpf": self.cpf,
            "rg": self.rg,
            "data_nascimento": self.data_nascimento.isoformat()  # Converte a data para string no formato ISO
        }

        # Adiciona os telefones se houverem
        if self.telefones:
            obj["telefones"] = [telefone.to_dict() for telefone in self.telefones]

        # Adiciona as apólices se houverem (caso queira fazer o mesmo com apólices)
        if self.apolices:
            obj["apolices"] = [apolice.to_dict() for apolice in self.apolices]

        return obj


class Apolice(Objeto):
    def __init__(self, seguradora, ramo, inicio_vigencia, fim_vigencia, premio_liquido, premio_total):
        self.seguradora = seguradora
        self.ramo = ramo
        self.premio_liquido = premio_liquido
        self.premio_total = premio_total
        self.vigencia_inicio = inicio_vigencia
        self.vigencia_fim = fim_vigencia

    def to_dict(self):
        return {
            "seguradora": self.seguradora,
            "ramo": self.ramo,
            "premio_liquido": self.premio_liquido,
            "premio_total": self.premio_total,
            "vigencia_inicio": self.vigencia_inicio.isoformat(),  # Converte a data para formato ISO
            "vigencia_fim": self.vigencia_fim.isoformat()
        }

class Produtor(Objeto):
    def __init__(self, nome):
        self.nome = nome

    def to_dict(self):
        return {
            "nome": self.nome
        }
