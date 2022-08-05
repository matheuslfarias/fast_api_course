from re import I
from typing import Optional
from pydantic import BaseModel

# Ao utilizar o BaseModel, o pydantic gera automaticamente os getters e setters,
# e outras funcionalidades muito poderosas

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    


cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=112, horas=58),
    Curso(id=2, titulo="Algoritmos e Lógica de Programação", aulas=87, horas=67),
]