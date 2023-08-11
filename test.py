import base64
from send_to_server import Database
test_database=Database("test@orfanidis.net.gr")
from gen import Encrypted_Communication
client=Encrypted_Communication(test_database)
#key=client.generate_key("test@orfanidis.net.gr")
#message = client.encrypt_message("hello", key)
#test_database.send_message("test@orfanidis.net.gr", message)

# Usage
messages = test_database.get_messages("test@orfanidis.net.gr")
for message in messages:
    message = base64.b64decode(message.get("message")).decode("utf-8").strip()
    print(message)
    print(client.decrypt_message(message))
