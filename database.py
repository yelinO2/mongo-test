import pymongo

class Database():
    mongo_db_uri = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient("""mongodb+srv://ye:123ye@simplenotecluster.cgkail7.mongodb.net/?retryWrites=true&w=majority""")
        Database.DATABASE = client['just-notes']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)