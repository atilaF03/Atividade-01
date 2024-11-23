from models.abstracts.pessoa import Pessoa
from models.endereco import Endereco  

class Juridico(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao_estadual: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nPessoa jurídica: "
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição estadual: {self.inscricao_estadual}\n"
        )