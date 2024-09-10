from enum import Enum 

import os 

class UnidadeFederativa(Enum):
    BAHIA = ("Bahia", "BA")
    SAO_PAULO = ("Sao Paulo", "SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "RJ")

    def __init__(self, nome: str, sigla: str):
        self._nome = nome
        self._sigla = sigla

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def sigla(self) -> str:
        return self._sigla

class Endereco : 
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, Uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.Uf = Uf

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"\nNúmero: {self.numero}"
                f"\nComplemento: {self.complemento}"
                f"\nCep: {self.cep}"
                f"\nCidade: {self.cidade}"
                f"\nUnidade Federativa: {self.Uf.value}"

               )

class Sexo (Enum):
    FEMININO = ("F", "Feminino")
    MASCULINO = ("M", "Masculino")

    def __init__(self, caractere: str, texto: str):
        self._caractere = caractere
        self._texto = texto

    @property
    def caractere(self) -> str:
        return self._caractere

    @property
    def texto(self) -> str:
        return self._texto



class Pessoa:
    def __init__(self, id: int, nome: str, dataNascimento: str, telefone: str, email: str, sexo: Sexo, endereco : Endereco ) -> None:
        self.id = id
        self.nome = nome 
        self.dataNascimento = dataNascimento
        self.telefone = telefone 
        self.email = email 
        self.sexo = sexo 
        self.endereco = endereco

    def __str__(self) -> str:
        """Equivalente ao toStr ing() do Java."""
        return (f"\nId: {self.id}"
                f"\nNome: {self.nome}"
                f"\nData de Nascimento: {self.dataNascimento}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nSexo:  {self.sexo.value}"
                f"\n========================"
                f"\nEndereço: {self.endereco}"
                )


os.system("cls||clear")

pessoa1 = Pessoa ( 45872, "MArta", "15/05/1986", "4575896", "maria@gmail.com", Sexo.FEMININO, Endereco ("Av Pajussara", "44", "Em Frente a Padaria Saraiva", "40715366", "Salvador", UnidadeFederativa.BAHIA))

print(pessoa1)

