import firebase_admin
from firebase_admin import credentials, firestore

class Database():

    def __init__(self):
        cred = credentials.Certificate("./personal-site-key.json")

        firebase_admin.initialize_app(cred)

        # Initialize Firestore
        self.db = firestore.client()

    def register_client(self, client_key, client_email):
        # Create a new document in a collection named "entries"
        collection_ref = self.db.collection('clients')
        new_doc_ref = collection_ref.document(client_email)
        
        new_doc_ref.set({
            'key': client_key,
            'email': client_email,
            'timestamp': firebase_admin.firestore.SERVER_TIMESTAMP  # Optional timestamp
        })

        print("Text entry stored in Firestore with ID:", new_doc_ref)
        return True
