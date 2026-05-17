from pydantic import BaseModel
from typing import Optional  

class Query(BaseModel):
    question:str
    context:Optional[str]=None
