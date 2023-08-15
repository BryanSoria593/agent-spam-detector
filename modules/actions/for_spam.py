from db.insertData import (
    add_user_with_id, select_user_id, insert_alert_user,
    insert_report_user, delete_document_temp
)
from modules.actions.email_processing import move_message_to_spam
from modules.actions.email_management import alert_user

def process_spam(from_, to, subject, body, prediction, id_group_mail, path, id_mail):
    try:
        to = list(set(to))
        # Conjunto para realizar un seguimiento de los usuarios únicos
        unique_users = set()
        add_user_with_id(to, id_group_mail, id_mail)
        data = select_user_id(id_group_mail)
        id_document = data[0]['_id']
        # Bandera para verificar si se ejecutó el bucle move_message_to_spam
        move_message_executed = False
        for i in data:
            user_spam = i['users']
            ids = i['idsTo']
            set(user_spam)
            set(ids)

            if len(user_spam) == len(ids):

                for user in user_spam:
                    for id_mail in ids:
                        move_message_to_spam(id_group_mail, user, id_mail)
                    # Agregar usuarios únicos al conjunto
                    unique_users.add(user)
                move_message_executed = True
        for unique_user in unique_users:
            alert_user(from_, unique_user, subject, body, prediction, path)
            insert_alert_user()
            insert_report_user()

        # Bandera para verificar si se ejecutó el bucle alert_user

        alert_user_executed = move_message_executed

        if move_message_executed and alert_user_executed:
            delete_document_temp(id_document)
            
    except Exception as e:
        print('Ha ocurrido un error en la función process_spam: ' + str(e))
        return False
