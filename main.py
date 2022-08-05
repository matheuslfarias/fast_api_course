from fastapi import FastAPI, Query
from fastapi import HTTPException
from fastapi import status, Path, Query, Header, Depends
from models import Curso, cursos
from fastapi.responses import Response
from typing import Optional,List, Any,Dict
from time import sleep

app = FastAPI(title="Api de cursos",
              version="0.0.1",
              description="Uma api para estudo do FastAPI")


# Dicionário de cursos, aqui serve como banco de dados.
def fake_db():
    try:
        print("Iniciando banco de dados...")
        sleep(1)
    finally:
        print("Banco de dados iniciado.")
        sleep(1)
        print("Fechando conexão com o banco de dados...")


# Criando primeiro  - GET
@app.get('/cursos',
         description="Retorna todos os cursos ou lista vazia",
         summary="Retorna todos os cursos",
         response_model=List[Curso],
         response_description="Cursos encontrados com sucesso")
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

# GET - ID
@app.get('/cursos/{id}')
async def get_curso(id: int = Path(default=None,
                                   title="ID do curso"),
                                   description="Deve ser entre 1 e 2",
                                   gt=0,
                                   lt=3,
                    db: Any = Depends(fake_db)):
    try:
        return cursos[id]
    except KeyError:  # Trata o erro de id não encontrado.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        
# POST 
@app.post('/cursos')
async def post_curso(curso: Curso, status_code=status.HTTP_201_CREATED, db: Any = Depends(fake_db)):
    next_id:int = len(cursos)+1
    curso.id = next_id
    cursos.append(curso)
    return curso

# PUT - UPDATE
@app.put('/cursos/{id}')
async def put_curso(id: int, curso: Curso, db: Any = Depends(fake_db)):
    if id in cursos:
        cursos[id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Não existe um curso com o {id}")

# DELETE
@app.delete('/cursos/{id}')
async def delete_curso(id: int, db: Any = Depends(fake_db)):
    if id in cursos:
        del cursos[id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Não existe um curso com o {id}")

@app.get('/calculadora')
async def calculadora(num1: int = Query(default=None,gt=5),
                      num2: int = Query(default=None,gt=10),
                      num3: Optional[int] = None,
                      x_geek: str = Header(default=None)):
    soma = num1 + num2 
    if num3:
        soma = soma+num3
        
    print(f"X-GEEK: {x_geek}")
    return {"resultado":soma}



    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000,debug=True,reload=True)
