from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, passwd, host, port, database, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = passwd
        HOST = host
        PORT = port
        DB = database
        COL = collection
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

        

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, searchData=None):
        if searchData is not None:
            data = list(self.database.animals.find(searchData))
        else:
            data = list(self.database.animals.find())
        
        return data
            
# Create method to implement the U in CRUD.
    def update(self, data, newData):
        if data is not None:
            updateData = self.database.animals.update_many(data, {"$set": newData})
            final = updateData.raw_result
            return final
    
        else:
            raise Exception("Nothing to update, because data parameter is empty")
 
# Create method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            removeData = self.database.animals.delete_many(data)
            final = removeData.raw_result
            return final
    
        else:
            raise Exception("Nothing to delete, because data parameter is empty")