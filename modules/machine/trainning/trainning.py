import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
import pandas as pd


file = "/root/agente-spam/modules/machine/data/1. final_dataset.csv"
df = pd.read_csv(file)

email_contents = df['text'].tolist()
labels = df['label'].tolist()

# Crear una instancia del vectorizador de características
vectorizer = CountVectorizer()

# Vectorizar el contenido de los correos electrónicos
email_vectors = vectorizer.fit_transform(email_contents)

# Crear una instancia del modelo Random Forest
classifier = RandomForestClassifier()

# Entrenar el modelo con los vectores de correos electrónicos y las etiquetas correspondientes
classifier.fit(email_vectors, labels)

# Guardar el modelo entrenado en un archivo
model = "/root/agente-spam/modules/machine/trainning/finalized_model.sav"
with open(model, 'wb') as f:
    pickle.dump(classifier, f)

# Guardar el vectorizador en un archivo
vector = "/root/agente-spam/modules/machine/trainning/vectorizer.pkl"
with open(vector, 'wb') as f:
    pickle.dump(vectorizer, f)
