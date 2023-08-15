from pymongo import MongoClient, errors
from datetime import datetime
from datetime import timedelta
import pandas as pd
from db.connection import connect
client = connect()
db = client["project"]

def get_emails_for_type(word):
    try:
        collection_name = 'user_filter_list'
        if collection_name not in db.list_collection_names():
            print('No se ha encontrado la colección user_filter_list')
            return []
        collection = db[collection_name]
        users = collection.find({'type_user': word}, {'_id': 0, 'email': 1})
        users_list = list(users)
        if not users_list:
            print('No se han encontrado usuarios en la base de datos')
            return []
        return [user['email'] for user in users_list]

    except errors.ConnectionFailure as e:
        print('Error al consultar los datos en la función get_emails_for_type:', str(e))
        return False

    except errors.OperationFailure as e:
        print('Error al consultar los datos en la función get_emails_for_type:', str(e))
        return False

def verify_user_black_list(from_):
    try:
        collection = db["user_filter_list"]
        user = collection.find_one({'email': from_,'type_user': 'black'})
        if not user:
            return False
        return True

    except errors.ConnectionFailure as e:
        print('Error al consultar los datos en la función verify_user_black_list:', str(e))
        return False

    except errors.OperationFailure as e:
        print('Error al consultar los datos en la función verify_user_black_list:', str(e))
        return False


