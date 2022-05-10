
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from faker import Faker
import bcrypt

fake = Faker()

# Establecer conexion con firebase
cred = credentials.Certificate("./credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# agregar datos
doc_ref = db.collection('users').document()

doc_ref.set({
    'firstName': fake.first_name(),
    'lastName': fake.last_name(),
    'email': fake.ascii_safe_email(),
    'username': fake.user_name(),
    'password': bcrypt.hashpw(fake.word(), bcrypt.gensalt(10))
})

# leer datos
users_ref = db.collection(u'users')
docs = users_ref.stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
