from re import I
from typing import Optional
from pydantic import BaseModel

# Ao utilizar o BaseModel, o pydantic gera automaticamente os getters e setters,
# e outras funcionalidades muito poderosas

class Curso(BaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int
    

    