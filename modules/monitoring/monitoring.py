import sys
from modules.machine.prediction.prediction import prediction_mail
from modules.actions.email_processing import (get_name_file_and_id, get_values_of_dictionary,
                                              read_email_content,  move_message_to_spam, display_msg)

from modules.parsing.file_processing import get_file_with_received, get_file_without_words, ignore_users, process_black_users, is_email_in_conversation, ignore_user_own_domains
from modules.parsing.ignore_directory import get_non_ignored_directory
from modules.actions.for_ham import process_ham
from modules.actions.for_spam import process_spam

def onCreated(event):
    try:
        path = event.src_path
        # ignorar la carpeta incoming donde guardan los mensajes categorizados como borradores
        path_without_words = get_non_ignored_directory(path)
        if path_without_words == False:
            return

        # ignorar los archivos que no contengan la palabra recibido en su nombre, lo que significa que es un borrador
        mail_with_received = get_file_with_received(path)
        if mail_with_received == False:
            return

        # ignorar los archivos que contengan las palabras agregadas en la función get_file_without_words en su contenido, lo que significa que es un correo de alerta
        # en su contenido, 
        mail_without_words = get_file_without_words(path)
        if mail_without_words == False:
            return

        id_mail, file_name = get_name_file_and_id(path)
        id_mail = str(id_mail)
        # esto regresa un diccionario con el contenido
        final_content_as_dictionary = read_email_content(path)

        # esta función recive el diccionario anterior y devuelve los datos formateados
        from_, to, subject, body, attachments, id_group_mail = get_values_of_dictionary(
            final_content_as_dictionary)

        verify_black_list = process_black_users(from_)
        if verify_black_list == True:
            print('El usuario '+from_+' que pertenece a la lista negra está enviando mensajes y se lo removió a spam')
            process_spam(from_, to, subject, body, 'spam',
                         id_group_mail, path, id_mail)

            return

        # ignorar a los usuarios que están en la lista blanca
        verify_ignore_users = ignore_users(path)
        if verify_ignore_users == True:
            print('El correo pertenece a la lista blanca')
            process_ham('ham')
            return

        verify_user_own_domains = ignore_user_own_domains(path)

        if verify_user_own_domains == True:
            process_ham('ham')
            print('El correo pertenece a un dominio propio')
            return


        verify_conversation = is_email_in_conversation(path)
        if verify_conversation == True:
            print('El correo pertenece a una conversación')
            process_ham('ham')
            return

        #display_msg(path, from_, to, subject, body,attachments, id_mail, id_group_mail)
        prediction = prediction_mail(body)

        if prediction == 'ham':
            print('Se ha detectado un correo ham de un dominio externo')
            process_ham(prediction)
            return

        elif prediction == 'spam':
            print('Se ha detectado un correo spam')
            process_spam(from_, to, subject, body, prediction,
                         id_group_mail, path, id_mail)
            return

    except Exception as e:
        print('Ha ocurrido un error en la función onCreated' + str(e))
        return


