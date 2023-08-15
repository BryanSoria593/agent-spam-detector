import jwt
from datetime import datetime, timedelta
import pytz
from config import KEY_JWT


def encode_token(payload, hours= None):
    # Obtener la zona horaria de Ecuador (GMT-5)
    timezone = pytz.timezone('America/Guayaquil')

    # Obtener la fecha y hora actual en la zona horaria de Ecuador
    now = datetime.now(timezone)

    # Calcular la fecha de expiración sumando una hora
    exp_time = now + timedelta(hours=hours)

    # Agregar la fecha de expiración al payload
    payload['exp'] = exp_time

    # Generar el token
    token = jwt.encode(payload, KEY_JWT, algorithm='HS256')    

    # Devolver el token como cadena
    new_token = token.decode('utf-8')
    formatted_token = new_token.strip("b'")

    return formatted_token