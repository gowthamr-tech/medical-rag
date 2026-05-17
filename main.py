from fastapi import FastAPI
from rag.generation import Generation
from schema.input import Query
from rag.retrieval import Retrieval

raj=FastAPI()
@raj.post("/ask")
def ask(query:Query):
    return Generation.callOpensourceModel(query.question)