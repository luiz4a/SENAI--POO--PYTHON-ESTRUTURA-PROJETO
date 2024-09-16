from models.unidadeFederativa import UnidadeFederativa 

class Endereco:
   

   def __init__(self, logradouro: str, numero : str, uf: UnidadeFederativa ,complemento: str, cep: str, cidade: str) -> None:
      self.logradouro = logradouro
      self.numero = numero
      self.complemento = complemento
      self.cep = cep 
      self.cidade = cidade 
      self.uf = uf
    
def __str__(self) -> str:
       return (
                f"\nLograduro: {self.logradouro}"
                f"\nNumero: {self.numero}"
                f"\nUnidade Federativa: {self.uf.nome}"
                f"\nUF: {self.uf.sigla}"
       )
