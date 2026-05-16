from pymilvus import MilvusClient

class Retrieval:
    db=MilvusClient("hello.db")

    db.create_collection(
        dimension=768,
        collection_name='demo'
    )
    print(db.list_collections())



