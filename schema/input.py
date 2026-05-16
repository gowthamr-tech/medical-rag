from pydantic import BaseModel  

class Query(BaseModel):
    question:str
    context:str
