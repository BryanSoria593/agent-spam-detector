import pickle

def prediction_mail(mensaje):
    # Cargar el modelo entrenado desde un archivo
    model = '/root/agente-spam/modules/machine/trainning/finalized_model.sav'

    with open(model, 'rb') as f:
        classifier = pickle.load(f)

    # Cargar el vectorizador desde un archivo
    vector = '/root/agente-spam/modules/machine/trainning/vectorizer.pkl'
    with open(vector, 'rb') as f:
        vectorizer = pickle.load(f)
    pruebas = vectorizer.transform([mensaje])
    preddiccion = classifier.predict(pruebas)
    return preddiccion[0]

