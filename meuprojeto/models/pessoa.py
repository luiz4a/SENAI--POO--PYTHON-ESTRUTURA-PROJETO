from models.endereço import Endereco
from models.sexo import Sexo


class Pessoa:
    def __init__(self, nome: str, idade:int, dataNascimento: str, telefone: str, email: str, sexo: Sexo, endereco: Endereco ) -> None:
        self.nome = nome 
        self.idade = idade 
        self.dataNasicmento = dataNascimento
        self.telefone = telefone
        self.email = email
        self.sexo = sexo 
        self.endereco = endereco 

    def __str__(self) -> str:
        return(f"\nNome: {self.nome}"
               f"\nIdade: {self.idade}"
               f"\nSexo: {self.sexo}"
               f"\nSexo: {self.sexo.caractere}"
               f"\nEndereço: {self.endereco}"
              )
    
    
    