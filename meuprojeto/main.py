import os 

from models.pessoa import Pessoa 
from models.sexo import Sexo 
from models.unidadeFederativa import UnidadeFederativa
from models.endereço import Endereco


os.system("cls||clear")

pessoa1= Pessoa("Maria", 45,"4521454", "45214521","jdfbbfjh@jkgh", Sexo.FEMININO,  
                Endereco("Rua Av Pajussara", "44", UnidadeFederativa.RIO_DE_JANEIRO, "Perto da padaria", "40715366", "Salvador"))
 

print(pessoa1)