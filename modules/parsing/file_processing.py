import mailparser
from db.select_data import get_emails_for_type, verify_user_black_list

def get_file_with_received(path):
    try:
        with open(path, 'r') as file:
            valids_words = ['Received']
            for line in file:
                if any(word in line for word in valids_words):
                    file.close()
                    return True
            file.close()
            return False
    except Exception as e:
        print('Ha ocurrido un error en la función get_file_with_received' + str(e))

def is_email_in_conversation(path):

    try:

        with open(path, "rb") as f:

            msg = mailparser.parse_from_bytes(f.read())    

            if not (msg.headers.get('In-Reply-To')):

                return False

                f.close()

            return True

            f.close()



    except Exception as e:

        print('Ha ocurrido un error en la función is_email_in_conversation' + str(e))

def ignore_users(path):
    try:
        valid_users = get_emails_for_type('white')
        with open(path, 'rb') as file:
            msg = mailparser.parse_from_bytes(file.read())
            from_ = msg.from_[0][1]
            if from_ in valid_users:
                return True           
            return False
    except Exception as e:
        print('Ha ocurrido un error en la función ignore_users' + str(e))
        return False

def process_black_users(from_):
    try:
        verify_invalid_user = verify_user_black_list(from_)        
        if not verify_invalid_user:
            return False        
        return True        

    except Exception as e:
        print('Ha ocurrido un error en la función process_black_users:', str(e))
        return False

def get_file_without_words(path):
    try:
        with open(path, 'rb') as file:
            valids_words = ['admin@mail.zimbrat.com',
                             'detected@mail.zimbrat.com']

            msg = mailparser.parse_from_bytes(file.read())
            from_ = msg.from_[0][1]
            to = [x[1] for x in msg.to]
            if all(word in valids_words for word in [from_] + to):
                return False
            return True

    except Exception as e:
        print('Ha ocurrido un error en la función get_file_without_words' + str(e))
def ignore_user_own_domains(path):
    try:
        with open(path, 'rb') as file:
            invalid_domains = ['@lalibertad.gob.ec']
            msg = mailparser.parse_from_bytes(file.read())
            from_ = msg.from_[0][1]
            if any(word in from_ for word in valids_words):
                return True
            return False            
    except Exception as e:
        print('Ha ocurrido un error en la función ignore_user_own_domains' + str(e))


def ignore_user_own_domains(path):

    try:

        with open(path, 'rb') as file:

            invalid_domains = ['@mail.zimbrat.com']

            msg = mailparser.parse_from_bytes(file.read())

            from_ = msg.from_[0][1]

            if any(word in from_ for word in invalid_domains):

                return True

            return False            

    except Exception as e:

        print('Ha ocurrido un error en la función ignore_user_own_domains' + str(e))
