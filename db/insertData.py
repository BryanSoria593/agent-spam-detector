from pymongo import MongoClient, errors
from datetime import datetime
from datetime import timedelta
import pandas as pd
from db.connection import connect
client = connect()
db = client["project"]

def insert_alert_user():
    try:
        collection_name = 'alert_sent_user'
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
        collection = db[collection_name]
        verify_insert = collection.insert_one(
            {'dateOfAnalysis': datetime.now(),
            'prediction':'spam'}
        )
        if not verify_insert:
            return False
        return True        
    except errors.ConnectionFailure as e:
        print('Error al insertar los datos en la función insert_alert_user:', str(e))
        return False
    except errors.OperationFailure as e:
        print('Error al insertar los datos en la función insert_alert_user:', str(e))
        return False

def insert_ham(prediction):
    try:
        collection_name = 'normal_mail'
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
        collection = db[collection_name]
        verify_insert = collection.insert_one(
            {
                'dateOfAnalysis': datetime.now(),
                'prediction': prediction
            })
        if not verify_insert:
            return False
        return True
    except errors.ConnectionFailure as e:
        print('Error al insertar los datos en la función insert_ham:', str(e))
        return False
    except errors.OperationFailure as e:
        print('Error al insertar los datos en la función insert_ham:', str(e))
        return False

def insert_report_user():
    try:
        collection_name = 'report_mail'
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
        collection = db[collection_name]
        verify_insert = collection.insert_one(
            {
                'dateOfAnalysis': datetime.now(),
                'prediction':'spam'
            })
        if not verify_insert:
            return False
        return True        
    except errors.ConnectionFailure as e:
        print('Error al insertar los datos en la función insert_report_user:', str(e))
        return False
    except errors.OperationFailure as e:
        print('Error al insertar los datos en la función insert_report_user:', str(e))
        return False

def add_user_with_id(users, idMail, id):
    try:
        collection_name = 'temp_ids_mail'
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
        collection = db[collection_name]
        existing_doc = collection.find_one({"globalId": idMail})
        if existing_doc:
            collection.update_one(
                {"globalId": idMail},
                {"$push": {"idsTo": id}}
            )
        else:
            collection.insert_one(
                {
                    'globalId': idMail,
                    'users': users,
                    'idsTo': [id]
                }
            )

    except errors.ConnectionFailure as e:
        print('Error al insertar los datos en la función insert_report_user:', str(e))
        return False
    except errors.OperationFailure as e:
        print('Error al insertar los datos en la función insert_report_user:', str(e))
        return False

def select_user_id(globalId):
    try:
        collection_name = 'temp_ids_mail'

        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)

        collection = db[collection_name]
        documents = collection.find({"globalId": globalId})

        return documents        
    except errors.ConnectionFailure as e:
        print('Error al insertar los datos en la función select_user_id:', str(e))
        return False

    except errors.OperationFailure as e:
        print('Error al insertar los datos en la función select_user_id:', str(e))
        return False

def delete_document_temp(_id):
    try:
        collection = db["temp_ids_mail"]
        collection.delete_one({"_id": _id})

    except Exception as e:
        print('Error al eliminar los datos:', str(e))
        return False
