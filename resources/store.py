from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {"Message": "Store not found."}, 404

    def post(self, name):
         
        if StoreModel.find_by_name(name):
            return {"Message": "Store already exists."}

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            {"Message": "An error occurred while writing to db."}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()
        return {"Message": "Store deleted."}


class StoreList(Resource):

    def get(self):
        return {"Stores": [store.json() for store in StoreModel.query.all()]}





