from db.insertData import insert_ham

def process_ham(prediction):
    try:
        insert_ham(prediction)
    except Exception as e:
        print('Ha ocurrido un error en la función process_ham: ' + str(e))
