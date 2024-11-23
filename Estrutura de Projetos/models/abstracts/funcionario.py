
from models.enum.setor import Setor
from models.enum.sexo import Sexo  
from models.endereco import Endereco
from models.abstracts.fisica import Fisica
from abc import ABC, abstractmethod

class Funcionario(Fisica, ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, data_nascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float) -> None:  
        super().__init__(nome, telefone, email, endereco, cpf, rg, data_nascimento, sexo)
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n\nFuncionário: "
            f"\nMatrícula: {self.matricula}"
            f"\nSetor: {self.setor.value}"
            f"\nSalário: {self.salario}"
        )
