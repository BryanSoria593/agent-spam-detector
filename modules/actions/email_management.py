import smtplib
from db.insertData import insert_alert_user
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from modules.middleware.generate_jwt import encode_token
import uuid
import random
import string

from cryptography.fernet import Fernet
from config import KEY_ENCRYPT, EMAIL_DETECTED, DOMAIN_SERVER

def add_random_letters(token_part):
        random_letters = ''.join(random.choices(string.ascii_letters, k=5))
        return random_letters + token_part + random_letters

def alert_user(from_, to, subject, body, prediction, path):
    try:
        from_address = EMAIL_DETECTED  # remitente
        to_addresses = to  # destinatario

        # Establecer conexión con el servidor SMTP
        server = smtplib.SMTP(DOMAIN_SERVER)

        email_subject = f"Correo detectado como {prediction} - detalles"

        f = Fernet(KEY_ENCRYPT)

        uuid_ = str(uuid.uuid4())
        uuid_bytes = uuid_.encode()

        encrypted_uuid = f.encrypt(uuid_bytes)
        prediction_ = prediction.encode()

        encrypted_prediction = f.encrypt(prediction_)
        path_ = path.encode()

        encrypted_path = f.encrypt(path_)

        token = encode_token({
            'uuid': encrypted_uuid.decode(),
            'prediction': encrypted_prediction.decode(),
            'path': encrypted_path.decode(),
        }, hours=480)

        parts = token.split('.')
        header = add_random_letters(parts[0])
        payload = add_random_letters(parts[1])
        signature = add_random_letters(parts[2])
        modified_token = '.'.join([header, payload, signature])

        # Construir el cuerpo del mensaje en formato HTML

        html_body = f"""
            <html>
                <body>
                    <p><b>**Este mensaje es generado automáticamente por un detector de spam, por favor no responda a este correo**</b></p>
                    <p><b> El correo ha sido redireccionado a la carpeta de spam.</b></p>
                    <p><b> Si considera que este correo no es spam, ignore este mensaje.</b></p>
                    <p>Los detalles del correo son los siguientes:</p>
                    <p>Desde: {from_}</p>
                    <p>Para: {to}</p>
                    <p><b>Asunto:</b> {subject}</p>
                    <p><b>Cuerpo:</b> {body}</p>
                    <p>Si desea reportar este correo, por favor haga clic en el siguiente botón para más detalles:</p>
                    <p>
                        <a href="http://localhost:5000/quarantine/validate/{modified_token}">
                        <button style="padding: 10px 20px; background-color: #800020; color: white; border: none; border-radius: 4px; cursor: pointer;">
                        Reportar</button></a>
                    </p>
                </body>
            </html>
        """

        # Crear el cuerpo del mensaje en formato MIME multipart (texto y HTML)

        message = MIMEMultipart("alternative")
        message["Subject"] = email_subject
        message["From"] = from_address
        message["To"] = to_addresses



        # Agregar la parte de texto y la parte de HTML al mensaje

        text_part = MIMEText(body, "plain")
        html_part = MIMEText(html_body, "html")
        message.attach(text_part)
        message.attach(html_part)
        # Enviar el mensaje a cada destinatario
        server.send_message(message)
        verify_insert = insert_alert_user()
        if not verify_insert:
            return False
        # Cerrar la conexión con el servidor
        server.quit()

        return True

    except Exception as e:
        print('Ha ocurrido un error en la función alert_user: ' + str(e))
        return False


