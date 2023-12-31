import firebase_admin
from firebase_admin import credentials, firestore
import base64
import ntplib

class Database():

    def __init__(self, email=None):
        cred = credentials.Certificate("../personal-site-key.json")

        firebase_admin.initialize_app(cred)

        # Initialize Firestore
        self.db = firestore.client()
        self.email=email
        self.ntp = ntplib.NTPClient()
    
    def register_client(self, client_key, email):
        # Create a new document in a collection named "entries"
        collection_ref = self.db.collection('clients')
        new_doc_ref = collection_ref.document(email)
        
        new_doc_ref.set({
            'key': base64.b64encode(client_key.encode('utf-8')),
            'email': email,
            'timestamp': int(self.ntp.request('europe.pool.ntp.org').tx_time * 1000)  # Optional timestamp
        })

        print("Text entry stored in Firestore with ID:", new_doc_ref)
        return True
    
    def set_email(self, email):
        self.email=email
    
    def send_message(self, client_email, message):
        collection_ref = self.db.collection('messages')
        other_user = collection_ref.document(client_email)
        new_message_for_other_user = {
            'message': base64.b64encode(message.encode('utf-8')),
            'from': self.email,
            'timestamp': int(self.ntp.request('europe.pool.ntp.org').tx_time * 1000)  # Optional timestamp
        }

        
        # Check if the other user's document exists
        if other_user.get().exists:
            # Retrieve the existing list of messages for the other user
            other_user_data = other_user.get().to_dict()
            other_user_messages = other_user_data.get('messages', [])
            # Add the new message to the other user's list
            other_user_messages.append(new_message_for_other_user)
            # Update the other user's document with the new message list
            other_user.set({'messages': other_user_messages}, merge=True)
        else:
            # Create the other user's document with the new message
            other_user.set({'messages': [new_message_for_other_user]})

    
    def get_messages(self, user_email):
        collection_ref = self.db.collection('messages')
        user_doc = collection_ref.document(user_email)
        user_data = user_doc.get().to_dict()
        if user_data and 'messages' in user_data:
            return [(base64.b64decode(message.get("message")).decode("utf-8").strip(), message.get("from")) for message in user_data['messages']]
        else:
            return []