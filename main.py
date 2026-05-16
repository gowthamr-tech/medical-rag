from fastapi import FastAPI
from pydantic import BaseModel  
from rag.generation import Generation

raj=FastAPI()
class Query(BaseModel):
    question:str
    context:str

@raj.post("/ask")
def ask(query:Query):
    return Generation.callOpensourceModel(query.context, query.question)