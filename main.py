from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status, Path
from models import Curso
from fastapi.responses import Response


app = FastAPI()


# Dicionário de cursos, aqui serve como banco de dados.

cursos = {
    1: {
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e Lógica de Programação",
        "aulas": 87,
        "horas": 67,
    }   
}

# Criando primeiro  - GET
@app.get('/cursos')
async def get_cursos():
    return cursos

# GET - ID
@app.get('/cursos/{id}')
async def get_curso(id: int = Path(default=None,
                                   title="ID do curso"),
                                   description="Deve ser entre 1 e 2",
                                   gt=0,
                                   lt=3):
    try:
        return cursos[id]
    except KeyError:  # Trata o erro de id não encontrado.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        
# POST 
@app.post('/cursos')
async def post_curso(curso: Curso,status_code=status.HTTP_201_CREATED):
    next_id:int = len(cursos)+1
    cursos[next_id] = curso
    del curso.id
    return curso

# PUT - UPDATE
@app.put('/cursos/{id}')
async def put_curso(id: int, curso: Curso):
    if id in cursos:
        cursos[id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Não existe um curso com o {id}")

# DELETE
@app.delete('/cursos/{id}')
async def delete_curso(id:int):
    if id in cursos:
        del cursos[id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Não existe um curso com o {id}")
        
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000,debug=True,reload=True)
