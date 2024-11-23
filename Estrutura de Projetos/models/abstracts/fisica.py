
from models.enum.sexo import Sexo  
from models.endereco import Endereco
from models.abstracts.pessoa import Pessoa
from abc import ABC, abstractmethod

class Fisica(Pessoa, ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, data_nascimento: str, sexo: Sexo) -> None:  
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        self.sexo = sexo

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCNPJ: {self.cpf}"  
            f"\nRG: {self.rg}"  
            f"\nData de nascimento: {self.data_nascimento}"  
            f"\nSexo: {self.sexo.texto}"  
            f"\nSigla: {self.sexo.caractere}"  
        )
