from models.enum.sexo import Sexo  
from models.abstracts.fisica import Fisica
from models.endereco import Endereco

class Cliente(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, data_nascimento: str, sexo: Sexo, protocolo_atendimento: int) -> None:  
        super().__init__(nome, telefone, email, endereco, cpf, rg, data_nascimento, sexo)
        self.protocolo_atendimento = protocolo_atendimento

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n\nProtocolo de atendimento: "
            f"\nNúmero: {self.protocolo_atendimento}"
        )