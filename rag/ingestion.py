import warnings
warnings.filterwarnings("ignore")
import os
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

from sentence_transformers import SentenceTransformer
model=SentenceTransformer("all-MiniLM-L6-v2")

from pymilvus import MilvusClient
class Ingestion:
    db=MilvusClient("hello.db")
    db.drop_collection("demo")
    db.create_collection(dimension=384,collection_name='Rockstar')
    # documents = [
    # "Diabetes is a chronic condition affecting blood sugar.",
    # "Hypertension is high blood pressure above 140/90.",
    # "Asthma causes breathing difficulty and wheezing.",
    # "Obesity increases risk of heart disease and diabetes.",
    # "Depression is a mood disorder with persistent sadness."]
    parents = [
        "Diabetes is a chronic condition affecting blood sugar. Type 1 is autoimmune. Type 2 is lifestyle related. Symptoms include fatigue and frequent urination.",
        "Hypertension is high blood pressure above 140/90. It causes heart disease and stroke. Managed by diet and medication.",
    ]
    def split_children(parents):
        sentences=parents.split(". ")
        return [s.strip() for s in sentences if s.strip()  ]
    # Build the data
    data=[]
    idx=0
    for p in parents:
        child=split_children(p)
        for c in child:
            vector=model.encode(c)
            data.append({
                "id":idx,
                "parent":p,
                "vector":vector.tolist(),
                "child":c
              }
        )
            idx+=1

    db.insert(
        collection_name="Rockstar",
        data=data,
    )
    print("Ingestion complete")