from enum import Enum 

import os
os.system("cls || clear")

class Sexo (Enum):
    MASCULINO = ("M", "Masculino")
    FEMININO = ("F", "Feminino")

    def __init__(self, texto: str, caractere: str) -> None:
        self.texto = texto
        self.caractere = caractere 
