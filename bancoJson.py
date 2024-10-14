import json
import os
from abc import ABC, abstractmethod
from Objetos import *

class GerenciadorObjetos:
    def __init__(self, arquivo_json):
        self.arquivo_json = arquivo_json
        # Se o arquivo não existir, cria um vazio
        if not os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, 'w') as f:
                json.dump([], f)
    
    def ler_objetos(self):
        """Lê todos os objetos do arquivo JSON"""
        with open(self.arquivo_json, 'r') as f:
            return json.load(f)

    def salvar_objetos(self, objetos):
        """Salva a lista de objetos no arquivo JSON"""
        with open(self.arquivo_json, 'w') as f:
            json.dump(objetos, f, indent=4)

    def adicionar_objeto(self, objeto):
        """Adiciona um novo objeto ao arquivo JSON"""
        objetos = self.ler_objetos()
        objetos.append(objeto.to_dict())
        self.salvar_objetos(objetos)

    def atualizar_objeto(self, identificador, novos_dados):
        """Atualiza os dados de um objeto pelo identificador (ex.: CPF ou outro campo único)"""
        objetos = self.ler_objetos()
        for obj in objetos:
            if obj.get("cpf") == identificador:  # Substitua "cpf" pelo campo que identifica o objeto
                obj.update(novos_dados)
                break
        self.salvar_objetos(objetos)

    def remover_objeto(self, identificador):
        """Remove um objeto do arquivo JSON pelo identificador"""
        objetos = self.ler_objetos()
        objetos = [obj for obj in objetos if obj.get("cpf") != identificador]  # Substitua "cpf" pelo campo de identificação
        self.salvar_objetos(objetos)

    def buscar_objeto(self, identificador):
        """Busca um objeto pelo identificador"""
        objetos = self.ler_objetos()
        for obj in objetos:
            if obj.get("cpf") == identificador:  # Substitua "cpf" pelo campo de identificação
                return obj
        return None

# Exemplo de uso

from datetime import date

# Criando um objeto Segurado
segurado = Segurado(nome="Carlos Silva", cpf="98765", rg="123456", data_nascimento=date(1985, 6, 15))

# Criando o gerenciador que manipula o arquivo 'objetos.json'
gerenciador = GerenciadorObjetos('objetos.json')

# Adicionando um novo segurado
gerenciador.adicionar_objeto(segurado)

# Atualizando o segurado com o CPF "98765"
gerenciador.atualizar_objeto("98765", {"nome": "Carlos Eduardo Silva"})

# Buscando o segurado pelo CPF
segurado_encontrado = gerenciador.buscar_objeto("98765")
print("Segurado encontrado:", segurado_encontrado)

# Removendo o segurado com o CPF "98765"
#gerenciador.remover_objeto("98765")
