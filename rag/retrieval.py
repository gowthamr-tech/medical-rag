import warnings
warnings.filterwarnings("ignore")
import os
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"
from pymilvus import MilvusClient
from sentence_transformers import SentenceTransformer
model=SentenceTransformer("all-MiniLM-L6-v2")
class Retrieval:
    db=MilvusClient("hello.db")

    def retrieve(self,question):
        query_vector=model.encode(question).tolist()
        results=self.db.search(
            collection_name="Rockstar",
            output_fields=["parent","child"],
            data=[query_vector],
            metric_type="L2"
            )
        seen=set()
        contexts=[]
        for r in results[0]:
            paren=r.entity.get("parent")
            if paren not in seen:
                seen.add(paren)
                contexts.append(paren)
        return contexts 
        # print("Results",results)

obj=Retrieval()
print(obj.retrieve("What is Tension?"))



