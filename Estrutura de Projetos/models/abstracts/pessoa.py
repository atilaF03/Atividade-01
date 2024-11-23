from abc import ABC, abstractmethod
from models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (
            f"Pessoa: "
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\n\nEndereço: {self.endereco}"
        )