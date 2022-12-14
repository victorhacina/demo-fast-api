from fastapi import FastAPI
#uvicorn main:app --reload
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/produs/{id}")    #CREATE
async def read_item(id: int):
    return {"message": f"Se creaza produsul {id}"}

@app.get("/produs/{id}")    #READ
async def read_item(id: int):
    return {"message": f"Se citeste produsul {id}"}

@app.put("/produs/{id}")    #UPDATE
async def read_item(id: int):
    return {"message": f"Se atualizeaza produsul {id}"}

@app.delete("/produs/{id}")    #DELETE
async def read_item(id: int):
    return {"message": f"Se sterge produsul {id}"}