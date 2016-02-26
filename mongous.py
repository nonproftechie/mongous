from pymongo import MongoClient

class SimpleMongoCRUDHandler:
    def __init__(self, database_name, collection_name, connection=None):
        self.client = MongoClient(connection)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def create(self, **kwargs):
        return self.collection.insert_one(kwargs)

    def create_many(self, documents):
        return self.collection.insert_many(documents)

    def read(self, **kwargs):
        return self.collection.find_one(kwargs)

    def read_many(self, **kwargs):
        return self.collection.find(kwargs)

    def update(self, doc, **kwargs):
        doc = dict(doc)
        del doc["_id"] # not allowed to edit
        mod = doc.copy()
        mod.update(kwargs)
        return self.collection.update_many(doc, {"$set": mod})

    def delete(self, **kwargs):
        return self.collection.delete_many(kwargs)
