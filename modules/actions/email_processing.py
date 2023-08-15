import mailparser
import subprocess

def move_message_to_spam(id_group_mail, to, id_mail):    
    try:
        email_user = to
        subprocess.run(["/opt/zimbra/bin/zmmailbox", "-z", "-m", email_user, "moveMessage", id_mail, "/Junk"])
    except Exception as e:
        print('Ha ocurrido un error en la función move_message_to_spam: ' + str(e))
        return False

def get_name_file_and_id(path):
    try:
        path = path.strip()
        file_name = path.rsplit('/', 1)[-1]
        id_mail = file_name[:file_name.find('-')]
        return id_mail, file_name
    except Exception as e:
        print('Ha ocurrido un error en la función get_name_file_and_id: ' + str(e))

def get_values_of_dictionary(dictionary):
    try:
        from_ = dictionary['from']
        to = dictionary['to']
        subject = dictionary['subject']
        body = dictionary['body']
        id_group_mail = dictionary['id_group_mail']
        attachments = dictionary['attachments']
        return from_, to, subject, body,  attachments, id_group_mail

    except Exception as e:    

        print('Ha ocurrido un error en la función get_values_of_dictionary' + str(e))

def read_email_content(path):
    try:
        with open(path, "rb") as f:

            email = {}
            msg = mailparser.parse_from_bytes(f.read())
            email['date'] = msg.headers.get('Date', 'Fecha no encontrada')
            email['from'] = msg.from_[0][1]
            email['to'] = [x[1] for x in msg.to]
            email['id_group_mail'] = msg.headers.get('Message-ID', 'Id no encontrado')
            email['subject'] = msg.headers.get(
                'Subject', 'Asunto no encontrado')

            # Se obtiene el cuerpo del mensaje, caso contrario se muestra un mensaje de que no hay mensaje

            body = msg.text_plain[0] if len(

                msg.text_plain) > 0 else 'No hay mensaje'
            body = delete_spaces_between_lines(body)
            email['body'] = body

            email['attachments'] = []
            for file in msg.attachments:
                email['attachments'].append(file.get('filename'))

            f.close()

            return email

    except Exception as e:

        print('Ha ocurrido un error en la función read_email_content' + str(e))

def delete_spaces_between_lines(text):

    return ''.join(text.splitlines())



def display_msg(path, from_, to, subject, body, attachments, id_mail, id_group_mail):

    try:
        print('*****************************')
        print('Ruta a leer ->  ', path)
        print('id del mensaje ->  ', id_group_mail)
        print("Remitente ->", from_)
        print("Receptores: ->", )
        for i in range(len(to)):
            print(f"    Receptor {i+1}: ", to[i])

        print("Subject ->", subject)
        print("Body ->", body)
        print("Files ->", attachments)
        print('idMail ->', id_mail)

    except Exception as e:
        print('Ha ocurrido un error en la función display_msg' + str(e))






