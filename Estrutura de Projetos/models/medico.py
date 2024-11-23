from models.enum.sexo import Sexo  
from models.enum.setor import Setor
from models.abstracts.funcionario import Funcionario
from models.endereco import Endereco

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, data_nascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float, crm: str) -> None:  
        super().__init__(nome, telefone, email, endereco, cpf, rg, data_nascimento, sexo, matricula, setor, salario)
        self.crm = crm

    def salario_final(self) -> float:
        resultado = self.salario  
        return resultado
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n\nProfissão: Médico"
            f"\nCRM: {self.crm}"  
        )