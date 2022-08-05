from multiprocessing.sharedctypes import Value
from re import I
from typing import Optional
from pydantic import BaseModel,validator


# Ao utilizar o BaseModel, o pydantic gera automaticamente os getters e setters,
# e outras funcionalidades muito poderosas

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int # mais de 12 aulas
    horas: int # mais de 10 horas
    
    @validator('titulo')
    def validar_titulo(cls,value):
        palavras = value.split(" ")
        # Validação 1
        if len(palavras) <3:
            raise ValueError("O título deve conter pelo menos 3 palavras")
        
        # Validação 1
        if value.islower():
            raise ValueError("O título deve conter pelo menos uma palavra em maiúsculo")
        
        # Validação 1
        if value.isupper():
            raise ValueError("O título deve conter pelo menos uma palavra em minúsculo")
        return value

    @validator('aulas')
    def validator_aulas(cls,value):
        if value < 12:
            raise ValueError("O curso deve ter mais de 12 aulas")
    
    @validator('horas')
    def validator_horas(cls,value):
        if value < 10:
            raise ValueError("O curso deve ter mais de 10 horas")

cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=112, horas=58),
    Curso(id=2, titulo="Algoritmos e Lógica de Programação", aulas=87, horas=67),
]