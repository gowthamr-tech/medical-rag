from fastapi import FastAPI
from rag.generation import Generation
from schema.input import Query

raj=FastAPI()
@raj.post("/ask")
def ask(query:Query):
    return Generation.callOpensourceModel(query.context, query.question)