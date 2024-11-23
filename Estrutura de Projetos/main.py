
from models.endereco import Endereco
from models.juridico import Juridico
from models.motoboy import Motoboy
from models.cliente import Cliente
from models.enum.unidade_federativa import UnidadeFederativa  
from models.enum.sexo import Sexo  
import os

os.system("cls||clear")

endereco_1 = Endereco("Rua tal", "19", "É alí", "1234-567", "Salvador", UnidadeFederativa.BAHIA)  
juridico_1 = Juridico("Caio", "1236-4678", "lucas@email", endereco_1, "123456", "123")

endereco_2 = Endereco("Rua ciclano", "06", "É aqui", "5123-512", "Rio Niterói", UnidadeFederativa.RIO_DE_JANEIRO)  
cliente_1 = Cliente("Gustavo", "4191-1481", "bira@email", endereco_2, "123.456.789.10", "52.014.418.41", "12/04/07", Sexo.MASCULINO, 123)

print(juridico_1)
print(cliente_1)
